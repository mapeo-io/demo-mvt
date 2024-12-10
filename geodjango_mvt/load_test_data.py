import random
from django.contrib.gis.geos import GEOSGeometry
from osgeo import ogr

from users.models import MyUser
from app.models import Building, STATUSES


file_path = "budynki3857.gpkg"

driver = ogr.GetDriverByName("GPKG")
data_source = driver.Open(file_path, 0)

layer = data_source.GetLayer(0)

region_user = {}

manager = MyUser.objects.create(
    email=f'manager@mapeo.io',
    first_name=f'Manager',
    last_name=f'Boss',
    type='mg'
)
manager.set_password('test')
manager.save()
print(f"created user {manager.email}, with password 'test'")

user_counter = 1
for feature in layer:
    geom = feature.GetGeometryRef()

    wkt = geom.ExportToWkt().replace('MULTIPOLYGON', 'POLYGON')
    wkt = wkt.replace("(((", "((").replace(")))", "))")

    if feature["JPT_NAZWA_"] not in region_user.keys():

        current_user, bo = MyUser.objects.get_or_create(
            email=f'seller{user_counter}@mapeo.io',
            first_name=f'Name{user_counter}',
            last_name=f'Lastname{user_counter}',
            type='sl'
        )
        current_user.set_password('test')
        current_user.save()

        print(f"created user {current_user.email}, with password 'test'")

        user_counter += 1
        region_user[feature["JPT_NAZWA_"]]=current_user

    Building.objects.create(
        seller=region_user[feature["JPT_NAZWA_"]],
        geom=GEOSGeometry(wkt, srid=3857),
        status=random.choice(list(STATUSES.keys())),
    )

data_source = None

print(f"Data loaded successfully!")
