from django.db import models

# Create your models here.

from django.contrib.gis.db import models as gis_models
from djangoapi.settings import EPSG_FOR_GEOMETRIES

class Calles(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    geom = gis_models.LineStringField(srid=int(EPSG_FOR_GEOMETRIES), blank=True, null=True)

    class Meta:
        db_table = 'p1\".\"calles'

class Semaforos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    geom = gis_models.PointField(srid=int(EPSG_FOR_GEOMETRIES), blank=True, null=True)

    class Meta:
        db_table = 'p1\".\"semaforos'

class Manzanas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    geom = gis_models.PolygonField(srid=int(EPSG_FOR_GEOMETRIES), blank=True, null=True)

    class Meta:
        db_table = 'p1\".\"manzanas'
