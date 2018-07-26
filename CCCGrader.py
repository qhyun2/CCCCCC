import tkinter as tk
import pygubu
import codeCompare

class Application:

    #store objects
    yearSelector = object()
    probSelect = object()
    testBench = object()
    master = object()

    def __init__(self, master):

        self.builder = builder = pygubu.Builder()
        self.master = master

        #load ui file
        builder.add_from_file('GUI.ui')

        #store objects
        self.probSelect = self.builder.get_object('probSelect', self.master)
        self.testBench = self.builder.get_object('testBench', self.master)
        self.yearSelector = self.builder.get_object('yearSelector', self.master)
        
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
root.resizable(False, False)
root.title('CCCCCC - Select Quesoaeaotion')

#codeCompare.test("2018q3sol.exe", "windows_data\S3\s3.3-02.in", b'temp')

root.mainloop()
