from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

def insert():
    conn = connect()
    cur = conn.cursor()
    cons = """
        INSERT INTO p1.semaforos
            (nombre, estado, tipo, geom)
        VALUES
            (%s, %s, %s,
            st_geometryFromText(%s, %s))
        RETURNING id
        """
    cur.execute(cons, [
        'Semaforo 1',
        'activo',
        'vehicular',
        'POINT(725000 4370000)',
        EPSG_CODE
    ])
    conn.commit()
    l = cur.fetchall()
    print(l)
    print(l[0][0])
    cur.close()
    conn.close()
    print("Inserted")


