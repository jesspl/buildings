import sys

from calles.insert import insert as insert_calles
from calles.select import select as select_calles
from calles.update import update as update_calles
from calles.delete import delete as delete_calles

from semaforos.insert import insert as insert_semaforos
from semaforos.select import select as select_semaforos
from semaforos.update import update as update_semaforos
from semaforos.delete import delete as delete_semaforos

from manzanas.insert import insert as insert_manzanas
from manzanas.select import select as select_manzanas
from manzanas.update import update as update_manzanas
from manzanas.delete import delete as delete_manzanas

def main():
    if len(sys.argv) >= 3:
        tableName = sys.argv[1]
        functionName = sys.argv[2]
    else:
        print("Error: You must give two parameters tableName and functionName.")
        sys.exit(0)

    if tableName not in ["calles", "semaforos", "manzanas"]:
        print("Error: The available table names are calles, semaforos, manzanas")
        sys.exit(0)

    if functionName not in ["insert", "select", "selectAsDict", "update", "delete"]:
        print("Error: The available function names are insert, select, selectAsDict, update, delete")
        sys.exit(0)

    if tableName == "calles":
        if functionName == "insert":
            insert_calles()
        elif functionName == "select":
            select_calles()
        elif functionName == "selectAsDict":
            select_calles(asDict=True)
        elif functionName == "update":
            id     = sys.argv[3] if len(sys.argv) > 3 else 1
            nombre = sys.argv[4] if len(sys.argv) > 4 else 'Calle actualizada'
            update_calles(id, nombre)
        elif functionName == "delete":
            delete_calles()

    elif tableName == "semaforos":
        if functionName == "insert":
            insert_semaforos()
        elif functionName == "select":
            select_semaforos()
        elif functionName == "selectAsDict":
            select_semaforos(asDict=True)
        elif functionName == "update":
            id     = sys.argv[3] if len(sys.argv) > 3 else 1
            nombre = sys.argv[4] if len(sys.argv) > 4 else 'Semaforo actualizado'
            update_semaforos(id, nombre)
        elif functionName == "delete":
            delete_semaforos()

    elif tableName == "manzanas":
        if functionName == "insert":
            insert_manzanas()
        elif functionName == "select":
            select_manzanas()
        elif functionName == "selectAsDict":
            select_manzanas(asDict=True)
        elif functionName == "update":
            update_manzanas()
        elif functionName == "delete":
            delete_manzanas()

if __name__ == "__main__":
    main()