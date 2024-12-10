# Demo: MVT with GeoDjango

This repository contains a working example of how to use Map Vector Tiles (MVT) with GeoDjango. It includes the code used in my presentation at Python Summit (Warsaw 2024).

## What does this demo do?

This demo contains final solution from my presentation.

1. **Create a database with PostGIS.**
2. **Set up a GeoDjango project.**
3. **Apply database migrations.**
4. **Load test data**: All buildings from the Powiat Grodziski region.
5. **Create test users** for the application.
6. **Run the Django development server** to showcase the functionality.

## How to start the demo

1. Build and start the PostGIS database:
   ```bash
   docker compose up mvt_db -d --build
   ```

2. Build and start the Django project:
   ```bash
   docker compose up mvt_django --build
   ```

## Useful Links

- [Mapbox TileBBox function](https://github.com/mapbox/postgis-vt-util/blame/master/src/TileBBox.sql)  
- [Coordinate Systems Overview (Esri)](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/coordinate-systems-difference/)
