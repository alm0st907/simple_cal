import os
import json
from Task import Task

class TaskWriter:
    #JSON file to be written to
    outfile ='\0'

    #JSON file constructor
    def __init__(self, fileName = "default.json"):
        self.outfile = open(fileName, "w+")
    
    #Accepts an array of tasks , and writes them to the JSON file
    def writeToJSON(self, tasksToWrite):
        data = []
        
        #Adds every value in the tasksToWrite List to data as a dictionary. Tasks without names are excluded
        for val in tasksToWrite:
            if val.toDictionary()['Task'] != "":
                data.append(val.toDictionary())

        json.dump(data, self.outfile)
        print("Writing to JSON file complete")
        

    #Writes a standard string to a text file, or any file that accepts strings
    def writeToText(self, stringToWrite):
        self.outfile.write(stringToWrite)
        print("writing to text file complete")
        
    #closes the file
    def closeFile(self):
        self.outfile.close()
