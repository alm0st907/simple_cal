import os


class Task:
    #task values
    taskName = ""
    taskExtraInfo = ""
    priority = 0
    month = 0
    day = 0
    year = 0
    hours = 0
    minutes = 0
    
    #Constructor for Task class
    def __init__(self, task = "", extraInfo = "", priorityV = 0, monthV = 0, dayV = 0, yearV = 0, hourV = 0, minuteV = 0):
        self.taskName = task
        self.taskExtraInfo = extraInfo
        self.priority = priorityV
        self.month = monthV
        self.day = dayV
        self.year = yearV
        self.hours = hourV
        self.minutes = minuteV

    #Generates a dictionary based on the values of the class
    def toDictionary(self):
        taskDict = {'Task': self.taskName , 'ExtraInfo':self.taskExtraInfo, 'Priority': self.priority, 'Month': self.month, 'Day':self.day, 'Year': self.year, 'Hours': self.hours, 'Minutes' : self.minutes}
        return taskDict

    #Generates a string based on the values of the task
    def toString(self):
        taskStr = self.taskName + " " + self.taskExtraInfo + " Priority: " + str(self.priority) + ", date: " + str(self.month) + "." + str(self.day) + "." + str(self.year) + ", time: " + str(self.hours) + ":" + str(self.minutes) + "\n"
        return taskStr

    #getters for all task values
    def getTaskName(self):
        return self.taskName

    def getExtraDet(self):
        return self.taskExtraInfo

    def getPriority(self):
        return self.priority

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getYear(self):
        return self.year

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    #setters
    def setTaskName (self, taskString):
        self.taskName = taskString
    
    def setTaskExtraDetails(self, newDetails):
        self.taskExtraInfo = newDetails

    def setPriority(self, priorityVal):
        self.priority = priorityVal

    def setMonth(self, monthVal):
        self.month = monthVal
    
    def setDay(self, dayVal):
        self.day = dayVal
    
    def setYear(self, yearVal):
        self.year = yearVal
    
    def setTime(self, timeVal):
        self.time = timeVal

    def setHours(self, hourVal):
        self.hours = hourVal

    def setMinutes(self, minuteVal):
        self.minutes = minuteVal


    