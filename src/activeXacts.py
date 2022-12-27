import os

activeXactPath = f"../utils/activeXacts.csv"
class activeXacts:
    def __init__(self):
        # check if activeXacts.csv exists
        # if it does, load it into memory
        # if it doesn't, create it
        self.xactId = 0
        if(os.path.exists(f"../utils/activeXacts.csv")):
            print("Active transactions file exists.")
        else:
            print("Creating active transactions file.")
            f= open(activeXactPath,"x")
            print("Active transactions file created.")
            with open(activeXactPath, 'w') as f:
                print("Writing header to active transactions file.")
                f.write("Transaction ID,Table Name,Row ID,Operation,Column Name,Old Value,New Value")
                f.write("\n")

    def addXact(self, xact):
        # Add a transaction to the active transaction list
        # Path: src/activeXacts.py
        with open(activeXactPath, 'a') as f:
            f.write(f"{xact.getXactId()},{xact.getTableName()},{xact.getRowId()},{xact.getOperation()},{xact.getColumnName()},{xact.getOldValue()},{xact.getNewValue()}")
            f.write("\n")

    def commitXact(self, xactIdToCommit):
        # Commit a transaction from the active transaction list
        # Path: src/activeXacts.py
        xact = self.getXact(xactIdToCommit)
        if(xact != None):
            # commit the transaction
            if(xact.operation == "INSERT"):
                # insert into the table

    def removeXact(commands):
        # Remove a transaction from the active transaction list
        # Path: src/activeXacts.py
        pass

    def getXact(xactId):
        # Get a transaction from the active transaction list
        # Path: src/activeXacts.py
        with open(activeXactPath, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if(line.split(",")[0] == xactId):
                    xact = xact(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4], line.split(",")[5], line.split(",")[6])
        return xact;

    def updateXact(commands):
        # Update a transaction in the active transaction list
        # Path: src/activeXacts.py
        pass

    def getXactStatus(commands):
        # Get the status of a transaction in the active transaction list
        # Path: src/activeXacts.py
        pass

class xact:
    def __init__(self, xactId, operation, tableName, rowId, columnName, oldValue, newValue):
        self.xactId = xactId
        self.operation = operation
        self.tableName = tableName
        self.rowId = rowId
        self.columnName = columnName
        self.oldValue = oldValue
        self.newValue = newValue

    def getXactId(self):
        return self.xactId

    def getOperation(self):
        return self.operation

    def getTableName(self):
        return self.tableName

    def getRowId(self):
        return self.rowId

    def getColumnName(self):
        return self.columnName

    def getOldValue(self):
        return self.oldValue

    def getNewValue(self):
        return self.newValue

    def setXactId(self, xactId):
        self.xactId = xactId

    def setOperation(self, operation):
        self.operation = operation

    def setTableName(self, tableName):
        self.tableName = tableName

    def setRowId(self, rowId):
        self.rowId = rowId

    def setColumnName(self, columnName):
        self.columnName = columnName

    def setOldValue(self, oldValue):
        self.oldValue = oldValue

    def setNewValue(self, newValue):
        self.newValue = newValue