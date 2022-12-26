'''
Stores a list of the tables in the database and their columns.
'''

catalogPath = "../utils/catalog.csv"

class Catalog:
    @staticmethod
    def getCatalogById(self, tableId):
        with open(catalogPath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip("\n").split(",")[0] == tableId:
                return line.strip("\n").split(",")
    
    def getCatalogByName(self, tableName):
        with open(catalogPath, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if line.strip("\n").split(",")[1] == tableName:
                return line.strip("\n").split(",")

    def addToCatalog(self, tableId, tableName, columns, isOptional, isKey):
        if(self.getCatalogByName(tableName) == None):
            if(len(columns) == len(isOptional) and len(columns) == len(isKey)):
                with open(catalogPath, 'a') as f:
                    f.write(f"{tableId},")
                    f.write(f"{tableName},")
                    f.write(f"{columns},")
                    f.write(f"{isOptional},")
                    f.write(f"{isKey},")
                    f.write("\n")
            else:
                raise Exception("The number of columns, isOptional, and isKey do not match.")
        else:
            raise Exception("Table already exists.")

    def removeFromCatalog(self,tableName):
        with open(catalogPath, 'r') as f:
            lines = f.readlines()
        with open(catalogPath, 'w') as f:
            for line in lines:
                if line.strip("\n") != tableName:
                    f.write(line)
