from projectWide import *


class Painting(tk.Canvas):

    def __init__(self, parent, relief=None, background=None, width=None,
                 height=None):
        tk.Canvas.__init__(self, parent, relief=relief, background=background,
                           width=width, height=height)
        self.parent = parent

    def drawCircle(self, x, y, radius, fill=None, outline=None):
        self.create_oval(x-radius/2, y-radius/2, x+radius/2, y+radius/2,
                         fill=fill, outline=outline)

    def drawRect(self, xMin, yMin, xMax, yMax, fill=None, outline=None):
        self.create_rectangle(xMin=xMin, yMin=yMin, xMax=xMax, yMax=yMax,
                              fill=fill, outline=outline)

    def drawBox(self, xMin, yMin, xMax, yMax, fill=None):
        #Horizontal
        self.create_line(xMin, yMin, xMax, yMin, fill=fill)
        self.create_line(xMin, yMax, xMax, yMax, fill=fill)
        #Vertical
        self.create_line(xMin, yMin, xMin, yMax, fill=fill)
        self.create_line(xMax, yMin, xMax, yMax, fill=fill)


class Tab(tk.Frame):
    # ###repeatVars taskSystem --> class TaskTab
    def __init__(self, parent, xMin=None, yMin=None, xMax=None, yMax=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        #Dimensions
        self.xMin, self.yMin, self.xMax, self.yMax = xMin, yMin, xMax, yMax
        self.height = self.yMax - self.yMin
        self.width = self.xMax - self.xMin

        #Setup UI
        self.config(bg='#F0F0F0')
        self.pack(fill=BOTH, expand=1)

        #Canvas setup
        self.myCanvas = Painting(self, relief=GROOVE, background='#303030',
                                 width=self.width,
                                 height=self.height)
        self.myCanvas.place(x=self.xMin, y=self.yMin)

