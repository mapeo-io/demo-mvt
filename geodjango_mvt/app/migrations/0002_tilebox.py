from django.db import migrations


class Migration(migrations.Migration):
    """
    „Copyright (c), Mapbox All rights reserved”
    https://github.com/mapbox/postgis-vt-util/tree/master?tab=BSD-3-Clause-1-ov-file#readme

    ### TileBBox ###
    Given a Web Mercator tile ID as (z, x, y), returns a bounding-box
    geometry of the area covered by that tile.
    __Parameters:__
    - `integer` z - A tile zoom level.
    - `integer` x - A tile x-position.
    - `integer` y - A tile y-position.
    - `integer` srid - SRID of the desired target projection of the bounding
    box. Defaults to 3857 (Web Mercator).
    __Returns:__ `geometry(polygon)`
    """

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """create or replace function TileBBox (z int, x int, y int, srid int = 3857)
                returns geometry
                language plpgsql immutable as
            $func$
            declare
                max numeric := 20037508.34;
                res numeric := (max*2)/(2^z);
                bbox geometry;
            begin
                bbox := ST_MakeEnvelope(
                    -max + (x * res),
                    max - (y * res),
                    -max + (x * res) + res,
                    max - (y * res) - res,
                    3857
                );
                if srid = 3857 then
                    return bbox;
                else
                    return ST_Transform(bbox, srid);
                end if;
            end;
            $func$;""",
        reverse_sql="drop function if exists TileBBox(z int, x int, y int, srid int) restrict;",
        elidable=False
        )
    ]