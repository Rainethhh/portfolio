from graphicsTools import *
from dataStorage import *


class Task:

    def __init__(self, name, taskType, startTime, endTime, reward=None, tags=None,
                 repeating=False, saveCopy=False):  # ###repeatVars
        self.name = name
        self.taskType = taskType
        self.startTime = startTime + rand.random()  # ###noise
        self.endTime = endTime + rand.random()  # ###noise
        self.reward = reward  # ###noise
        self.tags = tags
        self.repeating = repeating
        self.saveCopy = saveCopy



        self.varArray = dict(self.__dict__.items())
        for item in self.__dict__.values():
            print(item)
        print(self.varArray)
        self.saveToLibrary()

    def saveToLibrary(self):
        allData.taskLibrary.saveData(self.name, self.varArray)



# taskTab is the daughter class of Frame
class TaskTab(Tab):
    # ###repeatVars graphicsTools --> class Tab
    def __init__(self, parent, xMin=None, yMin=None, xMax=None, yMax=None):
        Tab.__init__(self, parent,
                     xMin=xMin, yMin=yMin, xMax=xMax, yMax=yMax)

        self.labelList = []

        # Task margins
        self.topRoom = 50
        self.rightRoom = 40
        self.leftRoom = 40
        self.bottomRoom = 50
        self.leftX = self.width - self.leftRoom
        self.bottomY = self.height - self.bottomRoom

        #Scroll location
        self.scrollX = 0
        self.scrollY = 0


        # Rectangle drawing ###default
        self.timeFocalX = 100
        self.rectHeight = 50
        self.rectSpacing = 10

        # rectangle scaling ###default
        self.pixelsPerHour = 100
        self.pixelsPerSecond = self.pixelsPerHour / 3600


        #Sorted tasks
        self.sortTasks()

        #refresh UI
        self.refreshUI()




    # def __init__(self, parent, grandParent):
    #     tk.Frame.__init__(self, parent)
    #     self.parent = parent
    #
    #     #Initialize UI variables
    #     self.varsUI()
    #
    #     #Go to UI setup
    #     self.initUI()

    # noinspection PyAttributeOutsideInit
    # def varsUI(self):
    #     # Main GUI dimensions
    #     self.xMin, self.yMin, self.xMax, self.yMax = 50, 50, 750, 700
    #     self.height = self.yMax-self.yMin
    #     self.width = self.xMax-self.xMin
    #
    #     #Task margins
    #     self.topRoom = 50
    #     self.rightRoom = 40
    #     self.leftRoom = 40
    #     self.bottomRoom = 50
    #     #extras
    #     self.leftX = self.width - self.leftRoom
    #     self.bottomY = self.height - self.bottomRoom
    #
    #
    #     #Rectangle drawing
    #     self.timeFocalX = 100  # ###default
    #     self.rectHeight = 50
    #     self.rectSpacing = 10
    #     #rectangle scaling
    #     self.pixelsPerHour = 100
    #     self.pixelsPerSecond = self.pixelsPerHour / 3600
    #
    #
    #
    # def initUI(self):
    #     self.sortedTasks = taskLibrary.sortedData('startTime')
    #     self.config(bg='#F0F0F0')
    #     self.pack(fill=BOTH, expand=1)
    #     # self.taskCanvas = tk.Canvas(self, relief=GROOVE, background='#303030',
    #     #                             width=self.xMax-self.xMin,
    #     #                             height=self.yMax-self.yMin)
    #     self.taskCanvas = Painting(self, relief=GROOVE, background='#303030',
    #                                width=self.xMax-self.xMin,
    #                                height=self.yMax-self.yMin)
    #     self.taskCanvas.place(x=self.xMin, y=self.yMin)

# ------ --  --- - --

        #self.taskCanvas.create_rectangle(70, 20, 120, 170, fill='#427BF5', outline='#427BF5')

        # Set tab background

        # Place title
        # taskTabTitle = tk.Label(master=self, text='Task Timeline',
        #                         fg='white', bg='black', width=10, height=10)
        # taskTabTitle.place(x=150, y=0)

        # Draw task rectangles


        # Draw line at present time
        pass

    def refreshUI(self):
        # self.varsUI()
        # self.initUI()

        self.sortTasks()
        self.drawTaskRects()

    def scroll(self, direction):
        self.myCanvas.delete("all")
        for label in self.labelList:
            label.destroy()
        if direction == 'scrollUp':
            self.scrollUp()
        if direction == 'scrollDown':
            self.scrollDown()
        if direction == 'scrollLeft':
            self.scrollLeft()
        if direction == 'scrollRight':
            self.scrollRight()

    def scrollUp(self):
        self.scrollY += 5
        self.drawTaskRects()

    def scrollDown(self):
        self.scrollY -= 5
        self.drawTaskRects()

    def scrollLeft(self):
        self.scrollX += 5
        self.drawTaskRects()

    def scrollRight(self):
        self.scrollX -= 5
        self.drawTaskRects()

    def sortTasks(self):
        self.sortedTasks = allData.taskLibrary.sortedData('startTime')
        return self.sortedTasks

    def drawOneTask(self, taskNum, taskName):
        # Task's temporary dictionary of values
        tD = allData.taskLibrary.singleObjectDict(taskName)

        #Get rectangle dimensions
        dimensions = self.taskDimensions(tD, taskNum)
        rx1 = dimensions[0] + self.scrollX
        ry1 = dimensions[1] + self.scrollY
        rx2 = dimensions[2] + self.scrollX
        ry2 = dimensions[3] + self.scrollY
        # baguette, shoes = dimensions[0, 1]
        # print(shoes)


        # Draw rectangle for each task
        self.myCanvas.create_rectangle(rx1, ry1, rx2, ry2, fill='#427BF5',
                                       outline='#427BF5')

        # Write task name
        taskLabel = tk.Label(self, text=taskName, bg='#F0F0F0')
        taskLabel.place(x=rx1 + 50, y=ry1 + 50, width=100, height=20)
        self.labelList.append(taskLabel)




    def drawTaskRects(self):

        #Draw background
        self.myCanvas.create_rectangle(self.rightRoom, self.topRoom,
                                       self.width-self.leftRoom,
                                       self.height-self.bottomRoom,
                                       fill='#303030', outline='#303030')

        # ---Loop performed for each task individually---
        taskNum = -1
        for taskName in self.sortedTasks:
            taskNum += 1
            self.drawOneTask(taskNum, taskName)

        #---Post loop, no longer task-specific---
        #Draw line at current time
        timeX = self.secondsToPixel(0)

        # self.taskCanvas.create_line(timeX, 25, timeX, 475,
        #                             fill='#F0F0F0')
        # self.taskCanvas.create_oval(timeX-2.5, 22.5, timeX+2.5, 27.5,
        #                             fill='#F0F0F0', outline='#F0F0F0')
        # self.taskCanvas.create_oval(timeX - 2.5, 472.5, timeX + 2.5, 477.5,
        #                             fill='#F0F0F0', outline='#F0F0F0')

        self.myCanvas.create_line(timeX, 25, timeX, 625,
                                  fill='#F0F0F0')
        self.myCanvas.drawCircle(timeX, 25, 5,
                                 fill='#F0F0F0', outline='#F0F0F0')
        self.myCanvas.drawCircle(timeX, 625, 5,
                                 fill='#F0F0F0', outline='#F0F0F0')


    def taskDimensions(self, taskDictionary, taskNumber):
        tD = taskDictionary

        # Rectangle vars
        rx1 = self.secondsToPixel(tD['startTime'], useEpoch=True)
        ry1 = self.topRoom + (self.rectSpacing + self.rectHeight) * taskNumber
        rx2 = self.secondsToPixel(tD['endTime'], useEpoch=True)
        ry2 = ry1 + self.rectHeight
        # Fit within boundaries
        rx1 = constrainVar(rx1, self.rightRoom, self.leftX)
        rx2 = constrainVar(rx2, self.rightRoom, self.leftX)
        ry1 = constrainVar(ry1, self.topRoom, self.bottomY)
        ry2 = constrainVar(ry2, self.topRoom, self.bottomY)

        return rx1, ry1, rx2, ry2

    def secondsToPixel(self, t, useEpoch=False):
        if useEpoch:
            return self.rightRoom + (t-time.time()) * self.pixelsPerSecond + self.timeFocalX
        return self.rightRoom + t * self.pixelsPerSecond + self.timeFocalX



class Graph:
    def __init__(self, saveCopy=False):
        self.saveCopy = saveCopy


class BountyGraph(Graph):
    pass








