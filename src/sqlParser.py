selectExample = "SELECT * FROM this";
import table as Table
import catalog as Catalog

class Parser:
    @staticmethod
    def queryToToken(sql):
        return sql.split();
    
    @staticmethod
    def tokenToCommand(table, tokens):
        if(tokens[0] == "SELECT"):
            # @TODO: Implement 4 types of JOINs
            pass
        elif(tokens[0] == "INSERT"):
            tableName = tokens[2]
            columns = tokens[3].split(",")
            values = tokens[5].split(",")
            table.insertInto(columns, values, tableName)
        elif(tokens[0] == "UPDATE"):
            pass
        elif(tokens[0] == "DELETE"):
            pass
        elif(tokens[0] == "CREATE"):
            '''
            CREATE TABLE table_name (
                column1 datatype,
                column2 datatype,
                column3 datatype,
            );
            '''
            tableName = tokens[2]
            columns = []
            types = []
            isOptional = []
            isKey = []
            for i in range(4, len(tokens)-1):
                if(tokens[i] != "PRIMARY"):
                    columns.append(tokens[i])
                    types.append(tokens[i+1])
                    isOptional.append(True)
                    isKey.append(False)
            table = Table(Catalog.getCatalogCount(), tableName, columns, types, isOptional, isKey)


    @staticmethod
    def parse(table, sql):
        tokens = Parser.queryToToken(sql)
        Parser.tokenToCommand(table, tokens)


