from tkinter import *
from tkinter import ttk
from view.nagivation_bar import NavBar
from view.question_field import QuestionField

        
class MainApp():
    def __init__(self, master, kb):
        print("hello")
        self.master = master
        self.kb = kb
        self.frame = Frame(self.master, bg="white")
        self.navbar = NavBar(self.master)
        
        self.frame.pack(side="top", fill='x', ipadx=10, ipady=10)
        intro_lbl = Label(self.frame, text="Welcome to the Study Program test for Turkish students \n"
                                        "who are interested in studying in The Netherlands.", font=("Arial", 12))
        intro_lbl.grid(column=0, row=0)
        self.questionField = QuestionField(self.master, self.kb)


    def onExit(self):
        self.frame.destroy()
        self.quit()