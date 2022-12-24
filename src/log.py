import enumDef as enum

logPath = "../utils/log.csv"

class logFile:
    def __init__(self):
        try:
            with open(logPath, 'r') as f:
                pass
        except FileNotFoundError:
            self.logSeq = 0
            self.prevLSN = None
            self.recordType = None
            self.transactionID = None
            self.pageID = None
            self.length = None
            self.offset = None
            self.oldData = None
            self.newData = None
            with open(logPath, 'w') as f:
                f.write("logSeq,prevLSN,recordType,transactionID,pageID,length,offset,oldData,newData")

    def __str__(self):
        return f"{self.logSeq},{self.prevLSN},{self.recordType},{self.transactionID},{self.pageID},{self.length},{self.offset},{self.oldData},{self.newData}"

class Log:
    def __init__(self, prevLSN, recordType, transactionID, pageID, length, offset, oldData, newData):
        self.prevLSN = prevLSN
        self.recordType = recordType
        self.transactionID = transactionID
        self.pageID = pageID
        self.length = length
        self.offset = offset
        self.oldData = oldData
        self.newData = newData
        with open(logPath, 'r') as f:
            self.logSeq = len(f.readlines())

genLog = Log(1, 0, enum.xactAction.UPDATE, 1, 1, 1, 1, "oldData", "newData")
genLog.writeLog("../utils/log.csv")
