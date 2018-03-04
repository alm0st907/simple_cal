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
        for val in tasksToWrite:
            if val.toDictionary()['Task'] != "":
                data.append(val.toDictionary())
           # datastore = taskToWrite.toDictionary()

        json.dump(data, self.outfile)
        #json.dump(datastore, self.outfile)
        #json.dump(,self.outfile)

    def closeFile(self):
        self.outfile.close()
