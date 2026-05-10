from core.myLib.geometryTools import WkbConversor, GeometryChecks

# Verificar si un punto está dentro de una manzana
pointWkt = 'POINT(725050 4370050)'

conv = WkbConversor()
conv.set_wkt_from_text(pointWkt)  # ✅

gc = GeometryChecks(conv.get_as_wkb())

# Verificar si el punto está dentro de alguna manzana
ids = gc.check_st_condition('p1.manzanas', 'st_contains')
print("ST_Contains:")
print(gc.get_relate_message())

# Verificar si la geometría es válida
print("\nIs valid:", gc.is_geometry_valid())