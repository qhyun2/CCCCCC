import tkinter as tk
import pygubu
import codeCompare

women = object()

class Application:

    #store objects
    yearSelecter = object()

    def __init__(self, master):

        self.builder = builder = pygubu.Builder()

        #load ui file
        builder.add_from_file('GUI.ui')

        #create the widget using a master as parent
        self.mainwindow = builder.get_object('probSelect', master)

        #make 2018 default selection instead of 0
        self.yearSelecter = builder.get_object('yearSelector', master)
        self.yearSelecter.set(2018)
        
        #link buttons though callback
        callbacks = {
            'J1': lambda: self.selection("J1"),
            'J2': lambda: self.selection("J2"),
            'J3': lambda: self.selection("J3"),
            'J4': lambda: self.selection("J4"),
            'J5': lambda: self.selection("J5"),
            'S1': lambda: self.selection("S1"),
            'S2': lambda: self.selection("S2"),
            'S3': lambda: self.selection("S3"),
            'S4': lambda: self.selection("S4"),
            'S5': lambda: self.selection("S5"),

        }
        builder.connect_callbacks(callbacks)

    #handle button click
    def selection(self, name):
        print(self.yearSelecter.get() + " " + name)
        # print(selected)


if __name__ == '__main__':
    
    root = tk.Tk()
    app = Application(root)

    #app settings
    root.resizable(False, False)
    root.title('CCCCCC - Select Question')

    codeCompare.test("2018q3sol.exe", "windows_data\S3\s3.3-02.in", b'temp')

    root.mainloop()
