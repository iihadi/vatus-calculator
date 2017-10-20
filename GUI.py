#VATUS GUI Mk2
from tkinter import *

"""
varS = IntVar()
Checkbutton(master, text="S", variable=varS).grid(column=0,row=1, sticky=W)
varU = IntVar()
Checkbutton(master, text="U", variable=varU).grid(column=1, row=1, sticky=W)
varV = IntVar()
Checkbutton(master, text="V", variable=varV).grid(column=2, row=1, sticky=W)
varA = IntVar()
Checkbutton(master, text="A", variable=varA).grid(column=3, row=1, sticky=W)
varT = IntVar()
Checkbutton(master, text="T", variable=varT).grid(column=4, row=1, sticky=W)
"""
class LabeledCheckbutton(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=1)

class LabeledCheckbutton2(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=2)

class LabeledCheckbutton3(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=3)

class LabeledCheckbutton4(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=4)

class LabeledCheckbutton5(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.checkbutton = Checkbutton(self)
        self.label = Label(self)
        self.label.grid(row=0, column=0)
        self.checkbutton.grid(row=0, column=5)

root = Tk()
labeledcb = LabeledCheckbutton(root)
labeledcb.label.configure(text="S")
labeledcb.grid(row=0, column=0)

labeledcb2 = LabeledCheckbutton2(root)
labeledcb2.label.configure(text="U")
labeledcb2.grid(row=1, column=0)

labeledcb2 = LabeledCheckbutton2(root)
labeledcb2.label.configure(text="V")
labeledcb2.grid(row=2, column=0)

labeledcb2 = LabeledCheckbutton2(root)
labeledcb2.label.configure(text="A")
labeledcb2.grid(row=3, column=0)

labeledcb2 = LabeledCheckbutton2(root)
labeledcb2.label.configure(text="T")
labeledcb2.grid(row=4, column=0)

root.title("VATUS")
mainloop()
