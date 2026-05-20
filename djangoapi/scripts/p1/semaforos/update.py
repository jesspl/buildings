from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

def update(id=1, nombre='Semaforo actualizado', estado='activo', tipo='vehicular'):
    conn = connect()
    cur = conn.cursor()
    cons = """
        UPDATE p1.semaforos 
        SET (nombre, estado, tipo, geom) = ROW(%s, %s, %s, st_geometryFromText(%s, %s))    
        WHERE id = %s
        """
    valuesList = [
        nombre,
        estado,
        tipo,
        'POINT(725000 4370000)',
        EPSG_CODE,
        int(id)
    ]
    cur.execute(cons, valuesList)
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Updated id:{id} nombre:{nombre}")