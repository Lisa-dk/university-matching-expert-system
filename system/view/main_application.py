
from tkinter import *
from tkinter import ttk

class NavBar():
    def __init__(self, master):
        self.master = master
        self.navFrame = Frame(self.master, bg="gray")
        self.setNavBar()
        self.navFrame.pack(side="top", fill='x')

        def setNavBar(self):  
            navLabel = Label(self.navFrame, text="PE", font="Bahnschrift 15", bg="#FF8700", fg="gray17", height=2, padx=20, pady=20)
            navLabel.pack(side="right", fill='x', ipadx=5, ipady=5)

class MainApp():
    def __init__(self, master):
        print("hello")
        self.master = master
        self.frame = Frame(self.master, bg="green")
        self.navbar = NavBar(self.master)

        self.frame.pack(side="top", fill='x', ipadx=10, ipady=10)
        intro_lbl = Label(self.frame, text="Welcome to the Study Program test for Turkish students \n"
                                        "who are interested in studying in The Netherlands.", font=("Arial", 12))
        intro_lbl.grid(column=0, row=0)


    def onExit(self):
        self.frame.destroy()
        self.quit()