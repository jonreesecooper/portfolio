#   Python Ver:     3.8.5
#
#   Author:         Jonathan Cooper
#
#   Purpose:        Student tracking list.  Demonstrating OOP, Tkinter, GUI module
#                   using Tkinter Parent and Child relationships
#
#   Tested OS:      This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
import student_tracking_gui
import student_tracking_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
        self.master = master
        self.master.minsize(635,350)
        self.master.maxsize(635,350)
        student_tracking_func.center_window(self,635,350)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        student_tracking_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
