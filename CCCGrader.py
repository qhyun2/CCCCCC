import tkinter as tk
from tkinter.font import Font
import pygubu
import glob
import os

import codeTester


class TestCaseManager:

    container = object()
    checkboxList = []
    varList={} #for retriving the state of boxs

    def __init__(self, filelist, container):
        self.container = container

        #clean previous state
        container.delete(1.0, tk.END)
        self.checkboxList = []

        for i in filelist:
            self.addCheckbox(i)

        self.selectAll()
    
    def addCheckbox(self, filename):
        newCheckbox = tk.Checkbutton(master=self.container)
        newCheckbox.config(text=filename)
        newCheckbox.config(bg='#5a6465')
        newCheckbox.config(activebackground='#5a6465')
        newCheckbox.config(font=Font(family="Microsoft Sans Serif", size=14))

        self.varList[filename] = tk.IntVar()
        newCheckbox.config(var=self.varList[filename])
        self.container.window_create(tk.INSERT, window=newCheckbox)
        self.checkboxList.append(newCheckbox)

    #gets a list of wanted files
    def getSelected(self):

        fileList = []

        for key, value in self.varList.items():
            if value.get():
                fileList.append(key)
        return fileList
    
    #mass modify functions
    def selectAll(self):
        for checkbox in self.checkboxList:
            checkbox.select()

    def deselectAll(self):
        for checkbox in self.checkboxList:
            checkbox.deselect()

class Application:

    #store objects
    yearSelector = object()
    probSelect = object()
    testBench = object()
    master = object()
    terminalScroller = object()
    testContainer = object()
    outputSelector = object()
    testControls = object()
    selectionButtons = object()

    #fonts
    headerFont = object()
    textFont = object()
    buttonFont = object()

    #test case manager
    tcm = object()

    def __init__(self, master):

        self.builder = builder = pygubu.Builder()
        self.master = master

        #load ui file
        builder.add_from_file('GUI.ui')

        #store objects
        self.probSelect = self.builder.get_object('probSelect', self.master)
        self.testBench = self.builder.get_object('testBench', self.master)
        self.yearSelector = self.builder.get_object('yearSelector', self.master)
        self.terminalScroller = self.builder.get_object('terminalScroller', self.master)
        self.testContainer = self.builder.get_object('testContainer', self.master)
        self.testControls = self.builder.get_object('testControls', self.master)
        self.outputSelector = self.builder.get_object('outputSelector', self.master)
        self.selectionButtons = self.builder.get_object('selectionButtons', self.master)

        """mainwindow config"""
        self.master.minsize(1000, 600)

        #init and place fonts
        self.headerFont = Font(family="Microsoft Sans Serif", size=35)
        self.textFont = Font(family="Microsoft Sans Serif", size=14)
        self.buttonFont = Font(family="Microsoft Sans Serif", size=27)
        self.yearSelector.config(font=self.textFont)
        self.outputSelector.config(font=self.textFont)

        #configure expansion 
        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)
        self.probSelect.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        self.testBench.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        self.terminalScroller.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        self.testContainer.grid(sticky=(tk.N, tk.S, tk.E, tk.W))


        #apply font and sticky settings
        for i in self.probSelect.winfo_children():
            if isinstance(i, tk.Button):
                i.config(font=self.buttonFont)
                i.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        for i in self.testBench.winfo_children():
            if isinstance(i, tk.Button):
                i.config(font=self.textFont)
        for i in self.testControls.winfo_children():
            if isinstance(i, tk.Button):
                i.config(font=self.textFont)
            i.grid(sticky=(tk.N, tk.S, tk.E, tk.W))
        for i in self.selectionButtons.winfo_children():
            if isinstance(i, tk.Button):
                i.config(font=self.textFont)


        self.outputSelector.grid(sticky=(tk.E, tk.W))
        self.showSelector()

        #create and connect callback functions
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
        'back': lambda: self.showSelector(),
        'test': lambda: self.test(),
        'testSel': lambda: self.testSel(),
        'selectAll': lambda: self.tcm.selectAll(),
        'deselectAll': lambda: self.tcm.deselectAll()
        }
        self.builder.connect_callbacks(callbacks)

    """gui event handlers"""

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
        self.master.title("CCCCCC - " +  str(yearSelected) + " " + questionSelected)
        fileList = glob.glob1('./data/' + str(yearSelected) + '/' + questionSelected + '/', '*.in')
        nameList = []
        
        for filename in fileList:
            name, _ = os.path.splitext(filename)
            nameList.append(name)

        self.tcm = TestCaseManager(nameList, self.testContainer)
    
    def test(self):
        print("Testing All")
    
    def testSel(self):
        print("Testing Sel")
        self.tcm.getSelected()

yearSelected = 2018
questionSelected = "J1"

root = tk.Tk()
application = Application(root)

#app settings
#root.resizable(False, False)


#codeTester.test("2018q3sol.exe", "windows_data\S3\s3.3-02.in", b'temp')

root.mainloop()
