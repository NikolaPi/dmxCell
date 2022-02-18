#!/usr/bin/python3
from csvConverter import *
from showLoader import *
import sys

version = "0.1.1"
print("DMXCell Version " + version + "\n\n")

csvExt="csv"
showExt = "dmxc"

fileLocation = input("CSV or DMXC File Location (with extension): ")
# validate the filepath
inputExt = fileLocation.split('.')[-1]
if len(fileLocation.split('.')) < 2:
    print("Invalid file name. Quitting program")
    sys.exit()

if inputExt in [csvExt, showExt, "json"]:
    if inputExt == csvExt:
        #get output file location
        outputLocation = input("Where should the DMXC output file go (don't type extension):")
        convertCSV(fileLocation, outputLocation + "." + showExt)
    else:
        dmxCom = input("What is the location of the DMX Device: ")
        loadShow(fileLocation, dmxCom)
else:
    print(inputExt)
    print("Invalid file extension. Quitting program")
    sys.exit()