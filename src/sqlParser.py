demoSQL = "SELECT * FROM this";

# break the string into tokens
def parseToTokens(sql):
    return sql.split();

print(parseToTokens(demoSQL))

class ruleSet:
    def insertInto(tableName, columns, values):
        return f"INSERT INTO {tableName} ({columns}) VALUES ({values})"