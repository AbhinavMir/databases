import os

class activeXacts:
    def __init__(self):
        # check if activeXacts.csv exists
        # if it does, load it into memory
        # if it doesn't, create it
        if(os.path.exists(f"../utils/activeXacts.csv")):
            print("Active transactions file exists.")
        else:
            print("Creating active transactions file.")
            tablePath = f"../utils/activeXacts.csv"
            f= open(tablePath,"x")
            print("Active transactions file created.")
            with open(tablePath, 'w') as f:
                print("Writing header to active transactions file.")
                f.write("Transaction ID,Table Name,Row ID,Operation,Column Name,Old Value,New Value")
                f.write("\n")

    def addXact(commands):
        # Add a transaction to the active transaction list
        # Path: src/activeXacts.py
        pass