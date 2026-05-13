from core.myLib.geoModelSerializer import GeoModelSerializer, GeomodelLinestringSerializer, GeomodelPolygonSerializer
from .models import Calles, Semaforos, Manzanas

from core.myLib.geoModelSerializer import GeoModelSerializer, GeomodelPolygonSerializer
from .models import Calles, Semaforos, Manzanas

class CallesSerializer(GeoModelSerializer):
    check_geometry_is_valid = True
    check_st_relation = False

    class Meta:
        model = Calles
        fields = GeoModelSerializer.Meta.fields + ['nombre', 'longitud', 'estado']

class SemaforosSerializer(GeoModelSerializer):
    check_geometry_is_valid = True
    check_st_relation = False

    class Meta:
        model = Semaforos
        fields = GeoModelSerializer.Meta.fields + ['nombre', 'estado', 'tipo']

class ManzanasSerializer(GeoModelSerializer):
    check_geometry_is_valid = True
    check_st_relation = False

    class Meta:
        model = Manzanas
        fields = GeoModelSerializer.Meta.fields + ['nombre', 'area', 'descripcion']