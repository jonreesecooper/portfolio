#   Python Ver:     3.8.5
#
#   Author:         Jonathan Cooper
#
#   Purpose:        Student tracking list.  Demonstrating OOP, Tkinter, GUI module
#                   using Tkinter Parent and Child relationships
#
#   Tested OS:      This code was written and tested to work with Windows 10

import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
import student_tracking_main
import student_tracking_gui

def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program","Are you sure you want to exit application?"):
        self.master.destroy()
        os._exit(0)

def create_db(self):
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_student_tracking( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );")
        conn.commit()
    conn.close()
    first_run(self)

def first_run(self):
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_student_tracking (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('Jon','Cooper','Jon Cooper','571-209-0880','jonreesecooper@gmail.com','Python'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_student_tracking""")
    count = cur.fetchone()[0]
    return cur,count

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fullname,col_phone,col_email,col_course FROM tbl_student_tracking WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.list2.delete(0,END)
            self.list2.insert(END, data[0])
            self.list2.insert(END, data[1])
            self.list2.insert(END, data[2])
            self.list2.insert(END, data[3])

def addToList(self):
    var_fname = self.text_fname.get()
    var_lname = self.text_lname.get()
    var_fname = var_fname.strip()
    var_lname = var_lname.strip()
    var_fname = var_fname.title()
    var_lname = var_lname.title()
    var_fullname = ('{} {}'.format(var_fname,var_lname))
    var_phone = self.text_phone.get().strip()
    var_email = self.text_email.get().strip()
    var_course = self.text_course.get().strip()
    if not "@" or not "." in var_email:
        messagebox.showerror("Invalid email error","'{}' is not a valid email address, \nPlease enter valid email address".format(var_email))       

    elif (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
        conn = sqlite3.connect('db_student_tracking.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_student_tracking WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:
                cursor.execute("""INSERT INTO tbl_student_tracking (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                self.list1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database.  Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all five fields.")

def onDelete(self):
    var_select = self.list1.get(self.list1.curselection())
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_student_tracking""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation","All information associated with ({}) \nwill be permanently deleted from database. \n\nProceed with deletion?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_student_tracking.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_student_tracking WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self)
                onRefresh(self)
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before deleting ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self):
    self.list2.delete(0,END)
    onRefresh(self)
    try:
        index = self.list1.curselection()[0]
        self.list1.delete(index)
    except IndexError:
        pass

def onClear(self):
    self.list2.delete(0,END)
    self.text_fname.delete(0,END)
    self.text_lname.delete(0,END)
    self.text_phone.delete(0,END)
    self.text_email.delete(0,END)
    self.text_course.delete(0,END)

def onRefresh(self):
    self.list1.delete(0,END)
    conn = sqlite3.connect('db_student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM tbl_student_tracking""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fullname FROM tbl_student_tracking""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.list1.insert(END,str(item))
                i = i + 1
    conn.close()

                



if __name__ == "__main__":
    pass
