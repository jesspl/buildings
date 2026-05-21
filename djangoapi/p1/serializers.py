from core.myLib.geoModelSerializer import GeoModelSerializer, GeomodelPolygonSerializer
from .models import Calles, Semaforos, Manzanas

class CallesSerializer(GeoModelSerializer):
    check_geometry_is_valid = True
    check_st_relation = True
    matrix9IM = 'T********'
    class Meta:
        model = Calles
        fields = GeoModelSerializer.Meta.fields + ['nombre', 'longitud', 'estado']
    def get_table_name(self):
        return '"p1"."calles"'

class SemaforosSerializer(GeoModelSerializer):
    check_geometry_is_valid = True
    check_st_relation = False
    class Meta:
        model = Semaforos
        fields = GeoModelSerializer.Meta.fields + ['nombre', 'estado', 'tipo']

class ManzanasSerializer(GeoModelSerializer):
    check_geometry_is_valid = True
    check_st_relation = True
    matrix9IM = 'T********'
    class Meta:
        model = Manzanas
        fields = GeoModelSerializer.Meta.fields + ['nombre', 'area', 'descripcion']
    def get_table_name(self):
        return '"p1"."manzanas"'
