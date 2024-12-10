from django.contrib.gis.db import models
from users.models import MyUser

STATUSES = {
    'new': 'never reached',
    'visited': 'after on-site visit',
    'wants': 'wants to buy',
    'dont': 'not willing to buy',
    'bought': 'bought already',
}

class Building(models.Model):

    seller = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    geom = models.PolygonField(srid=3857)
    status = models.CharField(max_length=10, choices=STATUSES, default="new")
    note = models.TextField(null=True)
