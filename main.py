#Jessica Roux
#Student ID: 2317255
#Chapman Email: jroux@chapman.edu
#Course: 408-01
#Assignment 4

import scrA4 as scr
import sys

# Execute and run program/functions
def runAssignment4():
    #Taking user input to create the csv file and the number of records the user wants to create
    # fileName = input("Please input the file name to be created: ")
    # numRecords = int(input("Please input the number of records to be created: "))

    arg1 = sys.argv[1]
    arg2 = int(sys.argv[2])

    scr.genData(arg1, arg2)
    scr.importData(arg1)
    print("\n")
    print("Success! Completed.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runAssignment4()

