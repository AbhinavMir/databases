'''
A class to write and read from files ../utils (in CSV format)
'''

import os
import csv
import sys
import time

class FileHandler:
    def appendToLogFile(Log, logFile):
        with open(logFile, 'a') as f:
            f.write(Log)
        
    def readFromLogFile(logFile):
        with open(logFile, 'r') as f:
            return f.read()
