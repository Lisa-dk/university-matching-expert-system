from tkinter import *
from view.pages.results_page import ResultsPage
from view.theme import Theme
from view.pages.information_page import InformationPage
from view.pages.trace_page import TracePage


class NavBar:
    HEIGHT = 4
    BUTTONS_Y = 5

    def __init__(self, master, MainApp):
        self.master = master
        self.MainApp = MainApp

        self.trace_page_button = None
        self.results_page_button = None
        self.test_page_button = None
        self.home_button = None
        self.top_frame = None

        self.set_top_bar()

    def set_top_bar(self):
        """
        Adds top bar to frame
        """
        self.top_frame = Frame(self.master, height=50, bg=Theme.NAV_BAR_BG)
        self.top_frame.pack(side="top", fill='x', ipady=self.HEIGHT)
        self.top_frame.pack_propagate(0)
        self.set_home_button()

    def set_home_button(self):
        """
        Adds 'home' (info page) to frame
        """
        self.home_button = Button(self.top_frame,
                                  text="Home",
                                  font=('Arial', 20, 'bold'),
                                  command=self.home,
                                  fg=Theme.BUTTON_FG_COLOUR,
                                  bg=Theme.NAV_BAR_BG,
                                  activeforeground=Theme.TEXT_COLOUR,
                                  activebackground=Theme.NAV_BAR_BG,
                                  bd=0,
                                  padx=2,
                                  pady=7,
                                  relief=RAISED)
        self.home_button.place(x=0, y=self.BUTTONS_Y)
        self.home_button.pack(side="left", pady=10)

    def set_results_page_button(self):
        """
        Adds button to navigate the results page
        """
        self.results_page_button = Button(self.top_frame,
                                          command=self.results,
                                          text="Results",
                                          font=('Arial', 20, 'bold'),
                                          fg=Theme.BUTTON_FG_COLOUR,
                                          bg=Theme.NAV_BAR_BG,
                                          activeforeground=Theme.TEXT_COLOUR,
                                          activebackground=Theme.NAV_BAR_BG,
                                          bd=0,
                                          padx=2,
                                          pady=7,
                                          relief=RAISED)
        self.results_page_button.place(x=0, y=self.BUTTONS_Y)
        self.results_page_button.pack(side="left")

    def set_trace_page_button(self):
        """
        Adds button to navigate the trace page
        """
        self.trace_page_button = Button(self.top_frame,
                                        command=self.trace,
                                        text="Trace",
                                        font=('Arial', 20, 'bold'),
                                        fg=Theme.BUTTON_FG_COLOUR,
                                        bg=Theme.NAV_BAR_BG,
                                        activeforeground=Theme.TEXT_COLOUR,
                                        activebackground=Theme.NAV_BAR_BG,
                                        bd=0,
                                        padx=2,
                                        pady=7,
                                        relief=RAISED)
        self.trace_page_button.place(x=0, y=self.BUTTONS_Y)
        self.trace_page_button.pack(side="left")

    def remove_results_button(self):
        """
        Removes results buttons
        """
        if self.results_page_button is not None:
            self.results_page_button.destroy()
            self.results_page_button = None

    def remove_trace_button(self):
        """
        Removes trace button
        """
        if self.trace_page_button is not None:
            self.trace_page_button.destroy()
            self.trace_page_button = None

    def home(self):
        """
        Sets home page
        """
        if self.MainApp.current_frame is not None and self.MainApp.current_frame != InformationPage:
            self.MainApp.current_frame.destroy()
            self.MainApp.initialise_home()

    def results(self):
        """
        Sets results page
        """
        if self.MainApp.current_frame is not None and self.MainApp.current_frame != ResultsPage:
            self.MainApp.current_frame.destroy()
            self.MainApp.initialise_results()

    def trace(self):
        """
        Sets trace page
        """
        if self.MainApp.current_frame is not None and self.MainApp.current_frame != TracePage:
            self.MainApp.current_frame.destroy()
            self.MainApp.initialise_trace()
