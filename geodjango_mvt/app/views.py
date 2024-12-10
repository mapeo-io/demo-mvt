from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.db import connection
from rest_framework.authtoken.models import Token


def login_view(request):
    return render(request, "login.html")


def map_view(request):
    return render(request, "map.html")


def map_vector_tiles(request, token, zoom, x, y):

    try:
        user = Token.objects.get(key=token).user

        with connection.cursor() as cursor:

            if user.is_manager():
                cursor.execute("""
                    SELECT ST_AsMVT(tile) FROM 
                    (SELECT status, ST_AsMVTGeom(geom::geometry, TileBBox(%s, %s, %s, 3857)) 
                    FROM app_building) AS tile""", [zoom, x, y])
            else:
                cursor.execute("""
                    SELECT ST_AsMVT(tile) FROM
                    (SELECT status, ST_AsMVTGeom(geom::geometry, TileBBox(%s, %s, %s, 3857))
                    FROM app_building WHERE seller_id=%s) AS tile""", [zoom, x, y, user.id])

            result = cursor.fetchone()
            if result is None or result[0] is None:
                tile = b''
            else:
                tile = bytes(result[0])

            return HttpResponse(tile, content_type="application/x-protobuf")

    except Token.DoesNotExist:
        return JsonResponse({'error': 'Invalid or missing token'}, status=401)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
