from os.path import exists
import sys, csv, json

def convertCSV(inputPath, outputPath):
    # number of non-dmx columns before dmx channels
    dmxPrefixColumns = 2
    # number of non-numeric columns before numeric columns
    numericPrefixColumns = 1

    #check if file exists
    if not exists(inputPath):
        print("File does not exist. Exiting program")
        sys.exit()
    else:
        print("Converting File...")

        with open(inputPath) as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            csvData = []
            for row in csvReader:
                csvData.append(row)

        #Convert strings to numbers
        for csvRow in range(len(csvData)):
            if csvRow < 1:
                #do nothing if it is the label row
                pass
            else:
                #convert numeric strings to numbers
                for csvColumn in range(len(csvData[csvRow])):
                    if csvColumn < numericPrefixColumns:
                        #do nothing if the column is a non-numeric column
                        pass
                    else:
                        csvData[csvRow][csvColumn] = int(csvData[csvRow][csvColumn])
        #remove label row from the data
        del csvData[0]

        #convert csvData to jsonData
        jsonData = json.dumps(csvData)
        print(jsonData)

        #write JSON to file 
        outputFile = open(outputPath, "w")
        outputFile.write(jsonData)
        outputFile.close
        print("created DXMC output file")