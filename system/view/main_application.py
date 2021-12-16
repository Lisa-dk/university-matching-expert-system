
from tkinter import *
from tkinter import ttk

class MainApp:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.menubar = Menu(self.master, tearoff=0)
        self.master.config(menu=self.menubar)

        fileMenu = Menu(self.menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        self.menubar.add_cascade(label="File", menu=fileMenu)

        self.frame.pack()
        intro_lbl = Label(self.frame, text="Welcome to the Study Program test for Turkish students \n"
                                        "who are interested in studying in The Netherlands.", font=("Arial", 12))
        intro_lbl.grid(column=0, row=0)


    def onExit(self):
        self.frame.destroy()
        self.quit()