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
import student_tracking_main
import student_tracking_func

def load_gui(self):
    self.label_fname = tk.Label(self.master,text="First Name: ")
    self.label_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.label_lname = tk.Label(self.master,text="Last Name: ")
    self.label_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.label_phone = tk.Label(self.master,text="Phone Number: ")
    self.label_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.label_email = tk.Label(self.master,text="Email: ")
    self.label_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.label_course = tk.Label(self.master,text="Current Course: ")
    self.label_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.label_student = tk.Label(self.master,text="Student: ")
    self.label_student.grid(row=0,column=2, padx=(0,0),pady=(10,0),sticky=N+W)
    self.label_stats = tk.Label(self.master,text="Stats: ")
    self.label_stats.grid(row=0,column=4,padx=(0,0),pady=(10,0),sticky=N+W)

    self.text_fname = tk.Entry(self.master,text="")
    self.text_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.text_lname = tk.Entry(self.master,text="")
    self.text_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.text_phone = tk.Entry(self.master,text="")
    self.text_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.text_email = tk.Entry(self.master,text="")
    self.text_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.text_course = tk.Entry(self.master,text="")
    self.text_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.list1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.list2 = Listbox(self.master,exportselection=0)
    self.list1.bind('<<ListboxSelect>>',lambda event: student_tracking_func.onSelect(self,event))
    self.scrollbar1.config(command=self.list1.yview)
    self.scrollbar1.grid(row=1,column=3,rowspan=9,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.list1.grid(row=1,column=2,rowspan=9,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    self.list2.grid(row=1,column=4,rowspan=9,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.button_submit = tk.Button(self.master,width=12,height=2,text="Submit",command=lambda: student_tracking_func.addToList(self))
    self.button_submit.grid(row=10,column=5,padx=(25,0),pady=(45,10),sticky=W)
    self.button_delete = tk.Button(self.master,width=12,height=2,text="Delete",command=lambda: student_tracking_func.onDelete(self))
    self.button_delete.grid(row=10,column=6,padx=(15,0),pady=(45,10),sticky=W)

    student_tracking_func.create_db(self)
    student_tracking_func.onRefresh(self)

if __name__ == "__main__":
    pass
    







if __name__ == "__main__":
    pass
