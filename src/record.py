'''
This module contains the Record class. Records are Tuple objects that store a column of data in the database.
'''
class Record:
    def __init__(self, recordID, pageID):
        self.recordID = recordID
        self.pageID = pageID