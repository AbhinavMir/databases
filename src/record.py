'''
This module contains the Record class. Records are Tuple objects that store a column of data in the database.
'''
class Record:
    def __init__(self, recordID, pageID, types, values, isKey):
        self.recordID = recordID
        self.pageID = pageID
        if(len(types) == len(values)):
            for i in range(len(types)):
                if(self.types[i] == "int"):
                    try:
                        self.values[i] = int(self.values[i])
                    except:
                        raise Exception("Value" + self.values[i] + "is not a Pythonic integer.")
                elif(self.types[i] == "str"):
                    self.values[i] = str(self.values[i])
                else:
                    raise Exception("Type" + self.types[i] + "is not supported.")
        elif(len(types) != len(values)):
            raise Exception("The number of types and values do not match.")
        else:
            raise Exception("An unknown error has occurred.")

        