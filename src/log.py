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

    def __str__(self):
        return f"{self.logSeq},{self.prevLSN},{self.recordType},{self.transactionID},{self.pageID},{self.length},{self.offset},{self.oldData},{self.newData}"

    def writeLog(self, logFile):
        # write to csv
        with open(logFile, 'a') as f:
            f.write(str(self)+"\n")


genLog = Log(1, 0, enum.xactAction.UPDATE, 1, 1, 1, 1, "oldData", "newData")
genLog.writeLog("../utils/log.csv")
