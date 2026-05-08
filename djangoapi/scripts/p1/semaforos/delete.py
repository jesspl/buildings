from myLib.connect import connect

def delete():
    conn = connect()
    cur = conn.cursor()
    cons = """
        DELETE FROM
            p1.semaforos  
        WHERE
            id = %s
        """
    valuesList = [1]
    cur.execute(cons, valuesList)
    print(cur.rowcount)
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted")