from tkinter import *
import tkinter as tk
from tkinter import filedialog
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master=master
        self.master.minsize(290,120)
        self.master.maxsize(290,120)
        self.master.title("Site Generator")
        self.master.configure(bg="#F0F0F0")
        self.label=tk.Label(self.master,text="Enter desired text and click 'Create' to create site.")
        self.label.grid(row=0,column=0,rowspan=1,columnspan=2,padx=(15,15),pady=(10,0),sticky=E+W)
        self.btn1 = tk.Button(self.master,width=12,height=1,text="Create",command=lambda: updateHeading(self))
        self.btn1.grid(row=2,column=0,padx=(60,0),pady=(10,0))
        self.text1 = tk.Entry(self.master,text="")
        self.text1.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(15,15),pady=(10,0),sticky=E+W)


def updateHeading(self):
    update = "<html><body><h1>"+self.text1.get()+"</h1></body></html>"
    print(update)
    file = open("basicsite.html","w")
    file.write(update)
    file.close()
    launch = webbrowser.open(url='basicsite.html',new=0,autoraise=True)
    return launch





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
