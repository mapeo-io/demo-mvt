from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('map', views.map_view),
    path('mvt/<str:token>/<int:zoom>/<int:x>/<int:y>', views.map_vector_tiles),
]


