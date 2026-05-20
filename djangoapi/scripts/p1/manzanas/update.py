from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

def update(id=1, nombre='Manzana actualizada', area=200, descripcion='Descripcion actualizada'):
    conn = connect()
    cur = conn.cursor()
    cons = """
        UPDATE p1.manzanas 
        SET (nombre, area, descripcion, geom) = ROW(%s, %s, %s, st_geometryFromText(%s, %s))    
        WHERE id = %s
        """
    valuesList = [
        nombre,
        float(area),
        descripcion,
        'POLYGON((725000 4370000, 725100 4370000, 725100 4370100, 725000 4370100, 725000 4370000))',
        EPSG_CODE,
        int(id)
    ]
    cur.execute(cons, valuesList)
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print(f"Updated id:{id} nombre:{nombre}")