class Table:

    # tableId, tableName, records[], columns[]
    def __init__(self, tableId, tableName, records, columns, isOptional, isKey):
        self.tableId = tableId
        self.tableName = tableName
        self.columns = columns
        self.isOptional = isOptional
        self.isKey = isKey
        self.rowCounter = 0
        # record dict with rowId
        self.records = {}
    
    def getColumnNames(self):
        # return column names and status of mandatory and key
        

        # for record in records:
        #     for column in columns:
        #         self.records[self.rowCounter][column] = record
        #     self.rowCounter += 1
    
    def getLatestRowId(self):
        return self.rowCounter

    def insertInto(self, columns, values, tableName):
        if(len(columns) == len(values)):
            # Append to the end of the table
        else:
            raise Exception("The number of columns and values do not match.")