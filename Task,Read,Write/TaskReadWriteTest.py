
import os
from Task import Task
from TaskReader import TaskReader 
from TaskWriter import TaskWriter



def build():
    writer = TaskWriter("def.json")
    
    
    task1 = Task("Finish testing Code","",15,3,3,2018)
    task2 = Task("Commit to GIT","Git Gud", 12,3,3,2018)
    task3 = Task()

    writer.writeToJSON([task1,task2,task3])
    #writer.writeToJSON(task2)
    #writer.writeToJSON(task3)
    writer.closeFile()
    reader = TaskReader("def.json")

    readInTasks = reader.readFromJSON()
    #readInTask2 = reader.readFromJSON()
    #readInTask3 = reader.readFromJSON()
   
   # print("test")
    for task in readInTasks:
        print("{0}".format((task.toString())))


build()
