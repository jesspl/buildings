from psycopg.rows import dict_row
from myLib.connect import connect
from myLib.p1Settings import EPSG_CODE

class callesOOP():
    def __init__(self):
        self.conn = connect()
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def insert(self):
        cons = """
            INSERT INTO p1.calles 
                (nombre, longitud, estado, geom)
            VALUES
                (%s, %s, %s,
                st_geometryFromText(%s, %s))
            RETURNING id
            """
        self.cur.execute(cons, [
            'Calle OOP',
            100,
            'activo',
            'LINESTRING(725000 4370000, 725100 4370100)',
            EPSG_CODE
        ])
        self.conn.commit()
        l = self.cur.fetchall()
        print(l)
        print(l[0][0])
        self.disconnect()
        print("Inserted")

    def select(self, asDict=False):
        if asDict:
            self.cur = self.conn.cursor(row_factory=dict_row)
        cons = """
            SELECT 
                id, nombre, longitud, estado, st_astext(geom)
            FROM 
                p1.calles
            WHERE
                id > %s
            """
        self.cur.execute(cons, [0])
        l = self.cur.fetchall()
        print(l)
        print('First row:')
        print(l[0])
        self.disconnect()
        print("Selected")

    def update(self):
        cons = """
            UPDATE p1.calles 
            SET (nombre, longitud, estado, geom) = ROW(%s, %s, %s, st_geometryFromText(%s, %s))    
            WHERE id = %s
            """
        self.cur.execute(cons, [
            'Calle OOP actualizada',
            200,
            'inactivo',
            'LINESTRING(725000 4370000, 725200 4370200)',
            EPSG_CODE,
            2
        ])
        self.conn.commit()
        print(self.cur.rowcount)
        self.disconnect()
        print("Updated")

    def delete(self):
        cons = """
            DELETE FROM p1.calles  
            WHERE id = %s
            """
        self.cur.execute(cons, [2])
        self.conn.commit()
        print(self.cur.rowcount)
        self.disconnect()
        print("Deleted")