import tkinter
from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,300))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')
        
        self.vardirectory = StringVar()
        self.varLdirectory = StringVar()
        
        self.lblDisplay =Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3,column=1,padx=(30,0),pady=(30,0))


        self.txtFdirectory =Entry(self.master,text=self.vardirectory,width=40, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtFdirectory.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0),sticky=N+E)

        self.lbldirectory =Label(self.master,text='',width=40,font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lbldirectory.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0))

        
        self.btnFName =Button(self.master,text='Dirctory', width=15, height=2, command='')
        self.btnFName.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.lblfiles =Label(self.master,text='Files:', width=15,  fg='black', bg='lightgray')
        self.lblfiles.grid(row=1,column=0,padx=(30,0),pady=(30,0))
        
        self.btnDirectory = Button(self.master, text = "Check for Dirctory", width=15, height=2, command=self.Dirctory)
        self.btnDirectory.grid(row=2, column=0, padx=(30,0),pady=(30,0))

        self.btnCancel = Button(self.master, text = "Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=2, padx=(30,0),pady=(30,0), sticky=SE)

    
    def Dirctory (self):
        #fn = self.varFName.get()
        fpath =filedialog.askdirectory()
        listPath= os.listdir(fpath)
        print(fpath)
        self.lbldirectory.config(text=listPath)
        self.txtFdirectory.insert(0,fpath)
                               
    def cancel (self):
        self.master.destroy()







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
