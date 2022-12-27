import sqlParser

def main():
    # Read the input file
    input_file = open("input.txt", "r")
    input_string = input_file.read()
    input_file.close()

    # Parse the input string
    sqlParser.parse(input_string)