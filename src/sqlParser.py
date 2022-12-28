selectExample = "SELECT * FROM users WHERE name = 'John'"
insertExample = "INSERT INTO users (name, age) VALUES ('Mackie', 23)"
updateExample = "UPDATE users SET name = 'Mackie' WHERE name = 'John'"
deleteExample = "DELETE FROM users WHERE name = 'John'"
import table as Table
import catalog as Catalog
import re

class Parser:

    def is_valid_sql(query):
        # Use a regular expression to check if the query is a SELECT, INSERT, UPDATE, DELETE, or CREATE statement
        return bool(re.match(r'^\s*(SELECT|INSERT|UPDATE|DELETE|CREATE)', query, re.I))

    @staticmethod
    def queryToToken(sql):
        return sql.split();
    
    def tokenToCommand(self,table, tokens, activeXacts):
        if(self.is_valid_sql(tokens[0]) == False):
            raise Exception("Invalid SQL command.")
        else:
            if(tokens[0] == "SELECT"):
                # @TODO: Implement 4 types of JOINs
                pass
            elif(tokens[0] == "INSERT"):
                tableName = tokens[2]
                columns = tokens[3].split(",")
                values = tokens[5].split(",")
                activeXacts.addInsert(tableName, columns, values)
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
            elif(tokens[0]=="COMMIT"):
                activeXacts.commit()

    @staticmethod
    def parse(table, sql):
        tokens = Parser.queryToToken(sql)
        Parser.tokenToCommand(table, tokens)

