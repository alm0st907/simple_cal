
import os
from Task import Task
from TaskReader import TaskReader 
from TaskWriter import TaskWriter



def build():
    task1 = Task("Finish testing Code","",15,3,3,2018)
    task2 = Task("Commit to GIT","Git Gud", 12,3,3,2018)
    task3 = Task()

    #Tests writing to JSON File
    writer = TaskWriter("def.json")
    writer.writeToJSON([task1,task2,task3])
    writer.closeFile()

    #Tests conversion of JSON to string, for conversion from JSON to another file
    reader = TaskReader("def.json")
    JSON2strTest = reader.JSONtoString()
    print("{0}".format(JSON2strTest))
    reader.closeFile()
    
    #Writes JSON string to a file
    writer2 = TaskWriter("jsonOutput.txt")
    writer2.writeToText(JSON2strTest)

    #tests conversion of JSON data back into Task Class, prints to show results
    reader2 = TaskReader("def.json")
    readInTasks = reader2.readFromJSON()
    reader2.closeFile()
    for task in readInTasks:
        print("{0}".format((task.toString())))


build()
