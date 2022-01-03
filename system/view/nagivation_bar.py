from tkinter import *

from view.question_field import QuestionField
from view.results_page import ResultsPage
from view.theme import Theme
from view.information_page import InformationPage


class NavBar:
    HEIGHT = 4
    BUTTONS_Y = 5

    def __init__(self, master, MainApp):
        self.results_page_button = None
        self.master = master
        self.MainApp = MainApp
        self.test_page_button = None
        self.home_button = None
        self.top_frame = None
        self.set_top_bar()

    def set_top_bar(self):
        self.top_frame = Frame(self.master, bg=Theme.NAV_BAR_BG)
        self.top_frame.pack(side="top", fill='x', ipady=self.HEIGHT)
        self.set_home_button()

    def set_home_button(self):
        self.home_button = Button(self.top_frame, text="Home", command=self.home, fg=Theme.BUTTON_TEXT,
                                  bg=Theme.NAV_BAR_BG, activeforeground="white", activebackground=Theme.NAV_BAR_BG,
                                  bd=0, padx=10)
        self.home_button.place(x=0, y=self.BUTTONS_Y)
        self.home_button.pack(side="left")

    def set_results_page_button(self):
        self.results_page_button = Button(self.top_frame, command=self.results, text="Results",
                                          fg=Theme.BUTTON_TEXT, bg=Theme.NAV_BAR_BG,
                                          activeforeground="white", activebackground=Theme.NAV_BAR_BG, bd=0, padx=10)
        self.results_page_button.place(x=0, y=self.BUTTONS_Y)
        self.results_page_button.pack(side="left")

    def remove_results_button(self):
        if self.results_page_button is not None:
            self.results_page_button.destroy()
            self.results_page_button = None

    def home(self):
        if self.MainApp.current_frame is not None and self.MainApp.current_frame != InformationPage:
            self.MainApp.current_frame.destroy()
            self.MainApp.initialise_home()

    def results(self):
        if self.MainApp.current_frame is not None and self.MainApp.current_frame != ResultsPage:
            self.MainApp.current_frame.destroy()
            self.MainApp.initialise_results()
