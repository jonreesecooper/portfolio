import shutil
import os
import time
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master
        self.master.minsize(440,320)
        self.master.maxsize(440,320)
        center_window(self,440,320)
        self.master.title("Daily File Transfer")
        self.master.configure(bg="#F0F0F0")
        self.label_1=tk.Label(self.master,text="Select source filepath")
        self.label_1.grid(row=0,column=0,padx=(15,0),pady=(10,0), sticky=W)
        self.btn1 = tk.Button(self.master,width=12,height=1,text="Source",command=lambda: getDir(self))
        self.btn1.grid(row=1,column=0,padx=(15,0),pady=(10,0), sticky=W)
        self.text1 = tk.Entry(self.master,width=50)
        self.text1.grid(row=2,column=0,padx=(15,15),pady=(10,0))
        self.label_2=tk.Label(self.master,text="Select destination filepath")
        self.label_2.grid(row=3,columnspan=2,padx=(15,0),pady=(10,0),sticky=W)
        self.btn2 = tk.Button(self.master,width=12,height=1,text="Destination",command=lambda: setDir(self))
        self.btn2.grid(row=4,column=0,padx=(15,0),pady=(10,0), sticky=W)
        self.text2 = tk.Entry(self.master,width=50)
        self.text2.grid(row=5,column=0,padx=(15,15),pady=(10,0))
        self.label_3=tk.Label(self.master,text="Run File Transfer")
        self.label_3.grid(row=6,column=0,padx=(15,0),pady=(10,0),sticky=W)
        self.btn3 = tk.Button(self.master,width=12,height=2,text="Run",command=lambda: timestamp(self))
        self.btn3.grid(row=7,column=0,padx=(15,0),pady=(10,0), sticky=W)


#   Center our window on user's computer
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2)) 
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

#   Find file path for desired source directory
def getDir(self):
    source = tk.filedialog.askdirectory()
    self.text1.insert(END,source)

#   Find file path for desired destination directory
def setDir(self):
    destination = tk.filedialog.askdirectory()
    self.text2.insert(END,destination)

#   Obtain list of files from source directory
def listoffiles(self):
    filelist = os.listdir(path = self.text1.get())
    return filelist

#   Time stamp last modified date of .txt files in source directory
#   Get current time, compare to time stamp
#   If time stamp within 24 hours of current time
#   Move files to destination directory
def timestamp(self):
    files = listoffiles(self)
    source = self.text1.get()+"/"
    newlist = []
    i = 0
    while i < len(files):
        abPath=os.path.join(source,files[i])
        result = abPath.endswith('txt')
        
        if result:
            mod_time = os.path.getmtime(abPath)
            cur_time = time.time()
            if mod_time >= (cur_time - 86400):
                newlist.append(files[i])
        i += 1
    for i in newlist:
        shutil.move(source+i,self.text2.get())
    try:
        notify = messagebox.showinfo("File Transfer Complete", "You may now close application")
        return notify
    except:
        pass



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
