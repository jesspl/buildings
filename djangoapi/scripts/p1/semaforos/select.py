from myLib.connect import connect
from psycopg.rows import dict_row

def select(asDict=False):
    conn = connect()

    if asDict:
        cur = conn.cursor(row_factory=dict_row)
    else:
        cur = conn.cursor()

    cons = """
        SELECT 
            id, nombre, estado, tipo, st_astext(geom)
        FROM 
            p1.semaforos
        WHERE
            id > %s
        """
    cur.execute(cons, [0])
    l = cur.fetchall()
    print(l)
    print('First row:')
    print(l[0])
    conn.commit()
    cur.close()
    conn.close()
    print("Selected")