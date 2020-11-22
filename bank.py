from projectWide import *


class Currency:
    def __init__(self, name, quantized=True, stashes=None):  # ###repeatVars
        self.name = name
        self.quantized = quantized
        self.stashes = stashes

        self.varArray = dict(self.__dict__.items())
        print(self.varArray)
        self.saveToLibrary()

    def saveToLibrary(self):
        currencyLibrary.saveData(self.name, self.varArray)



class Stash:
    def __init__(self, currency, amount, timeCreated):
        self.currency = currency
        self.amount = amount
        self.timeCreated = timeCreated
        self.ageSeconds = time.time() - timeCreated
        self.ageHours = self.ageSeconds * 3600

    def calcCurrentValue(self):
        #Use expiration graph for this
        pass



class ExpirationGraph(Graph):
    pass



#---Currency database---
# ###repeatVars
# currencyLibrary = DataLibrary('bank', ['name', 'quantized', 'stashes'])
#
# rustyCaps = Currency('rusty caps', quantized=True, stashes=None)


