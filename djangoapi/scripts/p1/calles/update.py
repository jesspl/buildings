from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

def update():
    conn = connect()
    cur = conn.cursor()
    cons = """
        UPDATE
            p1.calles 
        SET 
            (nombre, longitud, estado, geom) = ROW(%s, %s, %s, st_geometryFromText(%s, %s))    
        WHERE
            id = %s
        """
    valuesList = [
        'Calle actualizada',
        200,
        'inactivo',
        'LINESTRING(725000 4370000, 725200 4370200)',
        EPSG_CODE,
        1
    ]
    cur.execute(cons, valuesList)
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print("Updated")