from taskSystem import *
from bank import *
import userInput


# Initialize variables
def initializeVars():
    pass


def doCommand(event):
    actionConfirm = tk.Label(windowGuy, text='The action has been performed.')
    actionConfirm.pack()
    if event.char == 'x':
        exitProgram()
    else:
        global confirmExit
        confirmExit = False
    if event.char == 'c':
        #go to command list
        pass
    if event.char == 't':
        #go to token system
        pass


def displayTab(tabName):
    if tabName == 'taskTab':
        pass
        #displayGoalTL()


def exitProgram():
    global confirmExit
    if confirmExit:
        windowGuy.destroy()
    else:
        confirmExit = True


def main():
    updateTime()
    initializeVars()
    taskTabThingy = TaskTab(windowGuy, xMin=50, yMin=50, xMax=750, yMax=700)

    #set up binds
    windowGuy.bind('w', lambda x: taskTabThingy.scroll(userInput.taskBinds.followKey('w')))
    windowGuy.bind('a', lambda x: taskTabThingy.scroll(userInput.taskBinds.followKey('a')))
    windowGuy.bind('s', lambda x: taskTabThingy.scroll(userInput.taskBinds.followKey('s')))
    windowGuy.bind('d', lambda x: taskTabThingy.scroll(userInput.taskBinds.followKey('d')))
    windowGuy.mainloop()


main()
# mainButton = tk.Button(windowGuy, text='action')
# mainButton.bind('<Key>', doCommand)
# mainButton.pack(pady=50)

#print(time.gmtime())
