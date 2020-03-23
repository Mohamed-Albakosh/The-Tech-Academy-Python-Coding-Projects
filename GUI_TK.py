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
        
        self.varFName = StringVar()
        self.varLName = StringVar()
        
        


        self.txtBrowse =Entry(self.master,text=self.varFName,width=40, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBrowse.grid(row=0,column=1,columnspan=2,padx=(30,0),pady=(30,0),sticky=N+E)

        self.txtBrowse1 =Entry(self.master,text=self.varLName,width=40,font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtBrowse1.grid(row=1,column=1,columnspan=2,padx=(30,0),pady=(30,0),sticky=N+E)

        
        self.btnBrowse =Button(self.master,text='Browse...', width=15, height=2, command='')
        self.btnBrowse.grid(row=0,column=0,padx=(30,0),pady=(30,0))

        self.btnBrowse1 =Button(self.master,text='Browse... ', width=15, height=2, command='')
        self.btnBrowse1.grid(row=1,column=0,padx=(30,0),pady=(30,0))
        
        self.btnSubmit = Button(self.master, text = "Check for files", width=15, height=2, command=self.Browse)
        self.btnSubmit.grid(row=2, column=0, padx=(30,0),pady=(30,0))

        self.btnCancel = Button(self.master, text = "Close Program", width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=2, padx=(30,0),pady=(30,0), sticky=SE)

    
    def Browse (self):
        fn = self.varBrowse.get()
        
    
                               
    def cancel (self):
        self.master.destroy()







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
