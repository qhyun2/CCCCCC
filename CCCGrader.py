import tkinter as tk
from tkinter.font import Font
import pygubu
import codeCompare

class Application:

    #store objects
    yearSelector = object()
    probSelect = object()
    testBench = object()
    master = object()

    #fonts
    headerFont = object()
    textFont = object()
    buttonFont = object()

    def __init__(self, master):

        self.builder = builder = pygubu.Builder()
        self.master = master

        #load ui file
        builder.add_from_file('GUI.ui')

        #store objects
        self.probSelect = self.builder.get_object('probSelect', self.master)
        self.testBench = self.builder.get_object('testBench', self.master)
        self.yearSelector = self.builder.get_object('yearSelector', self.master)

        #mainwindow config
        #self.master.bind('<Configure>', self.resize)
        self.master.minsize(809, 500)

        #init and place fonts
        self.headerFont = Font(family="Microsoft Sans Serif", size=35)
        self.textFont = Font(family="Microsoft Sans Serif", size=20)
        self.buttonFont = Font(family="Microsoft Sans Serif", size=27)
        self.yearSelector.config(font=self.textFont)

        #configure expansion
        self.probSelect.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        self.testBench.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        for i in self.probSelect.winfo_children():
            if isinstance(i, tk.Button):
                i.config(font=self.buttonFont)
                i.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        
        #show window
        self.showSelector()

        callbacks = {
        'J1': lambda: self.selectionMade("J1"),
        'J2': lambda: self.selectionMade("J2"),
        'J3': lambda: self.selectionMade("J3"),
        'J4': lambda: self.selectionMade("J4"),
        'J5': lambda: self.selectionMade("J5"),
        'S1': lambda: self.selectionMade("S1"),
        'S2': lambda: self.selectionMade("S2"),
        'S3': lambda: self.selectionMade("S3"),
        'S4': lambda: self.selectionMade("S4"),
        'S5': lambda: self.selectionMade("S5"),
        'back': lambda: self.showSelector()
        }
        self.builder.connect_callbacks(callbacks)

    #show selection window
    def showSelector(self):
        self.probSelect.tkraise() 
        self.master.title('CCCCCC - Select Question')
        #make 2018 default selection instead of 0
        self.yearSelector.set(2018)

    #question has been selected
    def selectionMade(self, question):
        self.testBench.tkraise() 
        yearSelected = self.yearSelector.get()
        questionSelected = question
        self.master.title("CCCCCC - " +  str(yearSelected) + " " + question)

yearSelected = 2018
questionSelected = "J1"

root = tk.Tk()
application = Application(root)

#app settings
#root.resizable(False, False)


#codeCompare.test("2018q3sol.exe", "windows_data\S3\s3.3-02.in", b'temp')

root.mainloop()
