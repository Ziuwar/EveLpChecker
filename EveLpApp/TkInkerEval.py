# tkinker evaluation

#!/usr/bin/env python      
import tkinter as tk

class EveLpApp(tk.Frame):
    "The class EveLpApp defines the layout of the client side App"
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)                       
        self.createWidgets()

        #Method for the app layout creation
    def createWidgets(self):

        #Makes the main window and rows/colums flexible
        top=self.winfo_toplevel()                
        top.rowconfigure(0, weight=2)            
        top.columnconfigure(0, weight=2)         
        self.rowconfigure(0, weight=2)           
        self.columnconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)           
        self.columnconfigure(1, weight=1)
        
        #Creates the wiggets for the app
        self.TextField = tk.Text(self)
        self.TextField.grid(row = 0, column = 0, columnspan = 2, sticky = tk.E+tk.W+tk.N+tk.S)
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)            
        self.quitButton.grid(row = 1, column = 1, sticky = tk.E+tk.W+tk.N+tk.S)     
        #self.okButton = tk.Button(self, text='OK', command=self.quit)            
        #self.okButton.grid(row = 1, column = 0,sticky = tk.E+tk.W+tk.N+tk.S)

#Generates a instance of the EveLpApp class
app = EveLpApp()                       
app.master.title('EvE Lp Efficiency')    
app.mainloop()


