selectExample = "SELECT * FROM this";

class Parser:
    @staticmethod
    def queryToToken(sql):
        return sql.split();
    
    def tokenToCommand(self, table, tokens):
        if(tokens[0] == "SELECT"):
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



