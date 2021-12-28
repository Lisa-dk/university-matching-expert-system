from tkinter import *

from view.information_page import InformationPage


class NavBar:
    HEIGHT = 10
    BUTTONS_Y = 5

    def __init__(self, master, MainApp):
        self.master = master
        self.MainApp = MainApp
        self.test_page_button = None
        self.home_button = None
        self.top_frame = None
        self.set_top_bar()

    def set_top_bar(self):
        self.top_frame = Frame(self.master, bg="#768c90")
        self.top_frame.pack(side="top", fill='x', ipady=self.HEIGHT)
        self.set_home_button()
        self.set_test_page_button()

    def set_home_button(self):
        self.home_button = Button(self.top_frame, text="Home", command=self.restart, fg="white", bg="#768c90", bd=0, padx=10)
        self.home_button.place(x=0, y=self.BUTTONS_Y)
        self.home_button.pack(side="left")
    
    def set_test_page_button(self):
        self.test_page_button = Button(self.top_frame, text="Test", fg="white", bg="#768c90", bd=0, padx=10)
        self.test_page_button.place(x=0, y=self.BUTTONS_Y)
        self.test_page_button.pack(side="left")

    def restart(self):
        if self.MainApp.question_field is not None:
            self.MainApp.question_field.destroy()
            self.MainApp.question_field = None
            self.MainApp.initialise()
