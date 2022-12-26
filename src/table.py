import catalog
import os

catalog = catalog.Catalog()

class Table:
    def __init__(self, tableId, tableName, columns, isOptional, isKey):
        self.rowCounter = 0
        self.records = {}
        self.tableId = tableId
        self.tableName = tableName
        if(len(columns) == len(isOptional) and len(columns) == len(isKey)):
            print("The number of columns, isOptional, and isKey match.")
            self.columns = columns
            self.isOptional = isOptional
            self.isKey = isKey
            # write a new file
            if(os.path.exists(f"../utils/tables/{tableName}.csv")):
                print("Table exists.")
            else:
                print("Creating table.")
                tablePath = f"../utils/tables/{tableName}.csv"
                f= open(tablePath,"x")
                print("Table created.")
                with open(tablePath, 'w') as f:
                    print("Writing columns to table.")
                    for i in range(len(columns)):
                        f.write(f"{columns[i]},")
                    f.write("\n")
                catalog.addToCatalog(tableId, tableName, columns, isOptional, isKey)
    
    def getLatestRowId(self):
        return self.rowCounter

    @staticmethod
    def dropTable(tableName):
        tablePath = f"../utils/tables/{tableName}.csv"
        if(os.path.exists(tablePath)):
            os.remove(tablePath)
            catalog.removeFromCatalog(tableName)
        else:
            print("Table does not exist.")
            pass

    def insertInto(self, columns, values, tableName):
        tablePath = f"../utils/tables/{tableName}.csv"
        if(len(columns) == len(values)):
            self.records[self.rowCounter] = {}
            for i in range(len(columns)):
                self.records[self.rowCounter][columns[i]] = values[i]
            with open(tablePath, 'a') as f:
                for i in range(len(columns)):
                    f.write(f"{values[i]},")
                f.write("\n")
            self.rowCounter += 1
        else:
            raise Exception("The number of columns and values do not match.")


Table.dropTable("users")
table = Table(0, "users", ["name", "age"], [False, False], [True, False])
#self, tableId, tableName, columns, isOptional, isKey
table.insertInto(["name", "age"], ["John", 20], "users")