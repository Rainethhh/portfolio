from projectWide import *


# sandra = Task('popcan420', 'baseball band', time.time()-5000, time.time() + 10000, 7, 8)
# bagel = Task('bagel', 3, time.time()+3000, time.time() + 20000, 3)

class AllData:
    def __init__(self):
        self.taskLibrary = DataLibrary('tasks', ['name', 'taskType', 'startTime', 'endTime',
                                       'reward', 'tags', 'repeating', 'saveCopy'])
        self.currencyLibrary = DataLibrary('bank', ['name', 'quantized', 'stashes'])

    def generateData(self):

        ###pickle
        self.genTaskData()
        self.genCurrencyData()

    def genTaskData(self):

        self.taskLibrary.saveData('popcan420', {'name': 'popcan420', 'taskType': 'baseball band',
                                                'startTime': time.time() - 5000,
                                                'endTime': time.time() + 10000, 'reward': None,
                                                'tags': None, 'repeating': False, 'saveCopy': False})

        self.taskLibrary.saveData('bagel', {'name': 'bagel', 'taskType': 3,
                                            'startTime': time.time() + 3000,
                                            'endTime': time.time() + 20000, 'reward': None,
                                            'tags': None, 'repeating': False, 'saveCopy': False})

    def genCurrencyData(self):
        self.currencyLibrary.saveData('rusty caps', {'name': 'rusty caps', 'quantized': True,
                                                     'stashes': None})

allData = AllData()
allData.generateData()



