import os
import json
from Task import Task

class TaskReader:
    #The file values will be read from
    infile = '\0'
    
    #constructor for TaskReader
    def __init__(self, infileName = "default.json"):
        self.infile = open(infileName, "+r")
    
    #Function reads all task dictionaries from the JSON file, and returns an array of Task objects
    def readFromJSON (self):
        dataDict = json.load(self.infile)
        newTasks = []
        
        #Converts JSON data into Task classes within a list
        for taskDict in dataDict:
            newTasks.append(Task(taskDict['Task'],taskDict['ExtraInfo'],taskDict['Priority'],taskDict['Month'],taskDict['Day'],taskDict['Year'], taskDict['Hours'],taskDict['Minutes']))
    
        return newTasks
    
    def JSONtoString(self):
        dataDict = json.load(self.infile)
        JSONstr = ""

        i = 0
        for taskDict in dataDict:
            #Ensures that JSON data is properly formatted with commas between JSON values
            if i == 0:
                JSONstr = str(taskDict)
            else:
                JSONstr = JSONstr + "," + str(taskDict)
            i += 1
            
        #If there is more then one JSON value, properly formats string to mimic JSON file data
        if i > 1:
            JSONstr = "[" + JSONstr + "]"

        return JSONstr

    #closes file
    def closeFile(self):
        self.infile.close()