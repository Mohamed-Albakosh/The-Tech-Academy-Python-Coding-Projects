"""
   for searsh by put .txt for example in File extensin box the file is come on the lists boxs aftre
   that click Add to add to database ffter get from database
   for change dirctory first click check for dirctory to choose dirctory after click change dirctory to
   choose the destination
   contact me if there any quetion 
"""
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
import sqlite3
import shutil

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,550))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')
        
        self.vardirectory = StringVar()
        self.varFilex = StringVar()
        self.varfname = StringVar()
        
        self.lblDisplay =Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))


        self.txtFdirectory =Entry(self.master,text=self.vardirectory,width=40, font=("Helvetica", 16), fg='black', bg='white')
        self.txtFdirectory.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0),sticky=N+E)

        self.txtFname =Entry(self.master,text= self.varfname,width=40,font=("Helvetica", 16), fg='black', bg='white')
        self.txtFname.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0))
        
        self.txtfilex =Entry(self.master,text= self.varFilex,width=40,font=("Helvetica", 16), fg='black', bg='white')
        self.txtfilex.grid(row=2,column=1,columnspan=2,padx=(30,0),pady=(30,0))


        
        self.lblApath =Label(self.master,text='Absolute path:', width=15,fg='black', bg='lightgray')
        self.lblApath.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblfiles =Label(self.master,text='Files:', width=15,  fg='black', bg='lightgray')
        self.lblfiles.grid(row=1,column=0,padx=(30,0),pady=(30,0))

        self.lblfiles =Label(self.master,text='Files extension:', width=15,  fg='black', bg='lightgray')
        self.lblfiles.grid(row=2,column=0,padx=(30,0),pady=(30,0))

        #Define the listbox with a scrollbar and grid them
        self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=3,column=2,rowspan=6,columnspan=1,padx=(30,0),pady=(30,0),sticky=N+E+S)
        self.lstList1.grid(row=3,column=1,rowspan=6,columnspan=1,padx=(30,0),pady=(30,0),sticky=N+E+S+W)

        self.scrollbar2 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList2 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstList2.bind('<<ListboxSelect>>',lambda event: drill50_phonebook_func.onSelect(self,event))
        self.scrollbar2.config(command=self.lstList1.yview)
        self.scrollbar2.grid(row=3,column=2,rowspan=6,columnspan=1,padx=(30,0),pady=(30,0),sticky=N+E+S)
        self.lstList2.grid(row=3,column=2,rowspan=6,columnspan=1,padx=(30,0),pady=(30,0),sticky=N+E+S+W)
    
        
        self.btnDirectory = Button(self.master, text = "Check for Dirctory", width=15, height=2, command=self.Dirctory)
        self.btnDirectory.grid(row=9, column=0, padx=(30,0),pady=(30,0))

        self.btnCancel = Button(self.master, text = "Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=9, column=2, padx=(30,0),pady=(30,0), sticky=SE)

        self.btGetfrom = Button(self.master, text = "Get from Database", width=15, height=2, command=self.Getfrom)
        self.btGetfrom.grid(row=6, column=0, padx=(30,0),pady=(30,0), sticky=SE)

        self.btnCDirctory = Button(self.master, text = "Change Dirctory", width=15, height=2, command=self.CDirctory)
        self.btnCDirctory.grid(row=9, column=1, padx=(30,0),pady=(30,0), sticky=SE)
        

        self.btnAdd = Button(self.master, text = "Add", width=15, height=2, command=self.Add)
        self.btnAdd.grid(row=7, column=0, padx=(30,0),pady=(30,0), sticky=SE)
        
        self.btnSearch = Button(self.master, text = "Search by extension", width=15, height=2, command=self.Search)
        self.btnSearch.grid(row=8, column=0, padx=(30,0),pady=(30,0), sticky=SE)

    
    def Dirctory (self):
        #fn = self.varFName.get()
        fpath =filedialog.askdirectory()
        file=self.txtFname.get()
        os.path.join(fpath, file)
        joinpfile=os.path.join(fpath, file)
        #listPath= os.listdir(fpath)
        #print(fpath)
        #self.txtFname.insert(0,listPath)
        self.txtFdirectory.insert(0,joinpfile)
                               
    def cancel (self):
        self.master.destroy()

    def Search(self):
        str1= StringVar()
        extension=self.txtfilex.get()
        fpath =filedialog.askdirectory()
        file=self.txtFname.get()
        #listPath= os.listdir(fpath)
        #list_str = []
        for fil in os.listdir(fpath):
            if fil.endswith(extension):
                self.lstList1.insert(0,fil)
                joinpfile=os.path.join(fpath, fil)
                self.lstList2.insert(0,os.path.getmtime(joinpfile))
                
        
                
        #list_str.append(str1)
        print(list_str) 

    def Add(self):
        

        conn = sqlite3.connect('db_file_project.db')

        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS tbl_File(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                file_Name TEXT,\
                last_Update int\
                )")
            conn.commit()
        conn.close()

        
        conn = sqlite3.connect('db_file_project.db')
        with conn:
            cur = conn.cursor()
            sn=self.lstList1.size()
            values = self.lstList1.get(1)
            print(values)
            i=0
            print(sn)
            while i < sn:
                cur.execute("INSERT INTO tbl_File(file_Name,last_Update) VALUES (?,?)",\
                                         (self.lstList1.get(i),self.lstList2.get(i)))
                i=i+1
                print(i)
                    
            conn.commit()
        conn.close()

    def Getfrom(self):
        conn = sqlite3.connect('db_file_project.db')
        with conn:
            cur = conn.cursor()
            cur.execute("select file_Name  from tbl_File")
            varPerson = cur.fetchall()
            print(varPerson)
            for item in varPerson:
                self.lstList1.insert(0,item)
            cur.execute("select last_Update  from tbl_File")
            varPerson = cur.fetchall()
            for item in varPerson:
                self.lstList2.insert(0,item)                             
                    
            conn.commit()
        conn.close()

    def CDirctory(self):
        fileDirc=self.txtFdirectory.get()
        file=self.txtFname.get()
        fpath =filedialog.askdirectory()
        
        shutil.move(fpath, fileDirc) 
        
         
     
        





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
