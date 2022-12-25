import enumDef as enum
import os

logPath = "../utils/log.csv"
#logSeq,prevLSN,recordType,transactionID,pageID,length,offset,oldData,newData
logColumns = ["logSeq", "prevLSN", "recordType", "transactionID", "pageID", "length", "offset", "oldData", "newData"]
logData = {}

class logFile:
    def __init__(self):
        # check if log file exists
        if(os.path.exists(logPath)):
            # check if log file has been initialized
            with open(logPath, 'r') as f:
                if(f.readline() == "logSeq,prevLSN,recordType,transactionID,pageID,length,offset,oldData,newData\n"):
                    logData = helperFunctions.loadDataToDictionary()
                else:
                    with open(logPath, 'w') as f:
                        f.write("logSeq,prevLSN,recordType,transactionID,pageID,length,offset,oldData,newData\n")
                        f.write(f"0, NA, NA, NA, NA, NA, NA, NA, NA " + "\n")

class Log:
    def __init__(self, LSN, prevLSN, recordType, transactionID, pageID, length, offset, oldData, newData):
        self.LSN = LSN
        self.prevLSN = prevLSN
        self.recordType = recordType
        self.transactionID = transactionID
        self.pageID = pageID
        self.length = length
        self.offset = offset
        self.oldData = oldData
        self.newData = newData
        with open(logPath, 'a') as f:
            f.write(f"{self.LSN},{self.prevLSN},{self.recordType},{self.transactionID},{self.pageID},{self.length},{self.offset},{self.oldData},{self.newData}" + "\n")

    def __str__(self):
        return f"{self.LSN},{self.prevLSN},{self.recordType},{self.transactionID},{self.pageID},{self.length},{self.offset},{self.oldData},{self.newData}"+"\n"

class helperFunctions:
    def parseDataFromLog():
        with open(logPath, 'r') as f:
            data = f.readlines()
            data = [x.strip() for x in data]
            data = data[1:]
            return data
    
    def loadDataToDictionary():
        data = helperFunctions.parseDataFromLog()
        for i in range(len(data)):
            logData[i] = {}
            for j in range(len(logColumns)):
                logData[i][logColumns[j]] = data[i].split(',')[j]
        return logData
    
    def getLatestLSN():
        data = helperFunctions.parseDataFromLog()
        return len(data)-1

class Main:
    def initializeLogProcess():
        return logFile()
    
    def appendLog(LSN, prevLSN, recordType, transactionID, pageID, length, offset, oldData, newData):
        return Log(LSN, prevLSN, recordType, transactionID, pageID, length, offset, oldData, newData)
