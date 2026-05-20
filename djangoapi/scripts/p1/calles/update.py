from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

def update(id=1, nombre='Calle actualizada', longitud=200, estado='activo'):
    conn = connect()
    cur = conn.cursor()
    cons = """
        UPDATE p1.calles 
        SET (nombre, longitud, estado, geom) = ROW(%s, %s, %s, st_geometryFromText(%s, %s))    
        WHERE id = %s
        """
    valuesList = [
        nombre,
        float(longitud),
        estado,
        'LINESTRING(725000 4370000, 725200 4370200)',
        EPSG_CODE,
        int(id)
    ]
    cur.execute(cons, valuesList)
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Updated id:{id} nombre:{nombre}")