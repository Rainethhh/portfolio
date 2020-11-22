# Tags to use CTRL + F to quickly find in the project are denoted with
# three hashes (###) plus the tag name.
# List of hash tags:
# ###repeat: If something is changed here, it must also be changed elsewhere
# --> ###repeatVars means specifically that variables are re-typed
# ###noise: If a part of the code will require noise to make dictionaries 1:1
# ###default: A default value that will be changed later
# ###pickle: An area of code that will have pickling later implemented to assist it


import time as time
import tkinter as tk
from tkinter import BOTH, X, Y, GROOVE, FLAT
import random as rand


class DataLibrary:
    def __init__(self, name, dataTypes):
        self.name = name
        self.dataTypes = dataTypes
        self.dataArray = {}

        #Create iterable list of all object names
        self.objectNameList = []
        self.dataTypeLists = {}

        # Initiate nested data structures
        for dt in self.dataTypes:
            self.dataArray[dt] = {}
            self.dataTypeLists[dt] = []


    def saveData(self, objectName, valueList):
        #which variables are being added?
        self.objectNameList.append(objectName)

        for dt in self.dataTypes:
            self.dataArray[dt][objectName] = valueList[dt]
            self.dataTypeLists[dt].append(valueList[dt])


    def sortedData(self, dataType, reverseList=False, sortingKey=None):
        #---reverse key value pairs---

        #Initiate empty dictionary
        valNameDict = {}

        #list of values
        valueList = self.dataTypeLists[dataType]
        nameList = self.objectNameList

        #Create dictionary of reversed pairs
        for objectN in range(len(valueList)):
            valNameDict[valueList[objectN]] = nameList[objectN]

        #---Turn into sorted list of names---

        #Initialize empty list
        sortedNames = []

        #Sort values
        sortedVals = sorted(valueList, reverse=reverseList)

        #Use sorted values to make list of sorted names
        for value in sortedVals:
            name = valNameDict[value]
            sortedNames.append(name)

        return sortedNames

    def singleObjectDict(self, objectName):
        #Initialize empty dictionary

        thisObjectDict = {}
        for dataType in self.dataTypes:
            thisObjectDict[dataType] = self.dataArray[dataType][objectName]

        return thisObjectDict


class Graph:
    #Critical points ex: {0.33: {'upcoming': 200}, 0.66: {'upcoming': 100}}
    def __init__(self, graphType='logistic', criticalPoints=[], saveCopy=False):
        self.saveCopy = saveCopy
        self.graphType = graphType
        self.criticalPoints = criticalPoints


    def equation(self):
        if self.graphType == 'logistic':
            pass









def constrainVar(currentVal, minVal, maxVal):
    if currentVal > maxVal:
        return maxVal
    elif currentVal < minVal:
        return minVal
    else:
        return currentVal


def updateTime():
    global currentTime
    currentTime = time.time()


# Tkinter window system
windowGuy = tk.Tk()
windowGuy.title('Window Guy')
windowGuy.geometry('1500x750')

