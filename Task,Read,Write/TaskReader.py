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
        

        print("code passes load")
        newTasks = []
        print("code succesfully initializes newTasks")
        
        for taskDict in dataDict:
            newTasks.append(Task(taskDict['Task'],taskDict['ExtraInfo'],taskDict['Priority'],taskDict['Month'],taskDict['Day'],taskDict['Year'], taskDict['Hours'],taskDict['Minutes']))
        
        print("newTasks is loaded")

        return newTasks
    
    def closeFile(self):
        self.infile.close()