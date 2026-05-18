# from core.myLib.geometryTools import WkbConversor, GeometryChecks

# # Verificar si un punto está dentro de una manzana
# pointWkt = 'POINT(725050 4370050)'

# conv = WkbConversor()
# conv.set_wkt_from_text(pointWkt)  # ✅

# gc = GeometryChecks(conv.get_as_wkb())

# # Verificar si el punto está dentro de alguna manzana
# ids = gc.check_st_condition('p1.manzanas', 'st_contains')
# print("ST_Contains:")
# print(gc.get_relate_message())

# # Verificar si la geometría es válida
# print("\nIs valid:", gc.is_geometry_valid())

from core.myLib.geometryTools import WkbConversor, GeometryChecks

# 1. PUNTO dentro de MANZANA
print("=== PUNTO dentro de MANZANA ===")
pointWkt = 'POINT(725050 4370050)'
conv = WkbConversor()
conv.set_wkt_from_text(pointWkt)
gc = GeometryChecks(conv.get_as_wkb())
gc.check_st_condition('p1.manzanas', 'st_contains')
print(gc.get_relate_message())

# 2. CALLE intersecta con MANZANA
print("\n=== CALLE intersecta con MANZANA ===")
lineWkt = 'LINESTRING(725000 4370000, 725200 4370200)'
conv2 = WkbConversor()
conv2.set_wkt_from_text(lineWkt)
gc2 = GeometryChecks(conv2.get_as_wkb())
gc2.check_st_condition('p1.manzanas', 'st_intersects')
print(gc2.get_relate_message())