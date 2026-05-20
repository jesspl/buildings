import sys
from calles.callesOOP import callesOOP

def main():
    if len(sys.argv) == 3:
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
        b = callesOOP()
        if functionName == "insert":
            b.insert()
        elif functionName == "select":
            b.select()
        elif functionName == "selectAsDict":
            b.select(asDict=True)
        elif functionName == "update":
            b.update()
        elif functionName == "delete":
            b.delete()

if __name__ == "__main__":
    main()