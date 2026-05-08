from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

def update():
    conn = connect()
    cur = conn.cursor()
    cons = """
        UPDATE
            p1.manzanas 
        SET 
            (nombre, area, descripcion, geom) = ROW(%s, %s, %s, st_geometryFromText(%s, %s))    
        WHERE
            id = %s
        """
    valuesList = [
        'Manzana actualizada',
        200,
        'Descripcion actualizada',
        'POLYGON((725000 4370000, 725100 4370000, 725100 4370100, 725000 4370100, 725000 4370000))',
        EPSG_CODE,
        1
    ]
    cur.execute(cons, valuesList)
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print("Updated")