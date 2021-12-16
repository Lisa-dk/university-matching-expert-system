
from tkinter import *
from tkinter import ttk

class NavBar():
    HEIGHT = 10
    BUTTONS_Y = 5

    def __init__(self, master):
        self.master = master
        self.setTopBar()

    def setTopBar(self):
        self.topFrame = Frame(self.master, bg="#FF8700")
        self.topFrame.pack(side="top", fill='x', ipady=self.HEIGHT)
        self.setHomeButton()
        self.setTestPageButton()
    
    def setHomeButton(self):
        self.homeButton = Button(self.topFrame, text="Home", bg="blue", padx=10)
        self.homeButton.place(x=0, y=self.BUTTONS_Y)
        self.homeButton.pack(side="left")
    
    def setTestPageButton(self):
        self.testPageButton = Button(self.topFrame, text="Test", bg='blue', padx=10)
        self.testPageButton.place(x=0, y=self.BUTTONS_Y)
        self.testPageButton.pack(side="left")
      
        
class MainApp():
    def __init__(self, master):
        print("hello")
        self.master = master
        self.frame = Frame(self.master, bg="white")
        self.navbar = NavBar(self.master)

        self.frame.pack(side="top", fill='x', ipadx=10, ipady=10)
        intro_lbl = Label(self.frame, text="Welcome to the Study Program test for Turkish students \n"
                                        "who are interested in studying in The Netherlands.", font=("Arial", 12))
        intro_lbl.grid(column=0, row=0)


    def onExit(self):
        self.frame.destroy()
        self.quit()