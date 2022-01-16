from tkinter import *
import os

from model.knowledge_base import KnowledgeBase
from view.pages.information_page import InformationPage
from view.nagivation_bar import NavBar
from view.pages.question_field import QuestionField
from view.pages.results_page import ResultsPage
from view.pages.trace_page import TracePage
from view.theme import Theme


class MainApp:
    def __init__(self, master):
        self.master = master
        self.kb = None
        self.current_frame = None

        self.navbar = NavBar(self.master, self)

        # self.top_frame = Frame(self.master, height=20, bg="#8C8984")
        # self.top_frame.pack(side="bottom", fill='x', ipady=2)
        # self.top_frame.pack_propagate(0)

        self.initialise_kb()
        self.initialise_home()

    def initialise_kb(self):
        self.kb = KnowledgeBase()
        print(self.kb.user_kb)

    def initialise_home(self):
        self.current_frame = InformationPage(self, self.master)

    def start_test(self):
        self.current_frame = QuestionField(self.master, self.kb, self)
        self.make_file()
    
    def add_results_page_button(self):
        if self.navbar.results_page_button is None:
            self.navbar.set_results_page_button()

    def add_trace_page_button(self):
        if self.navbar.trace_page_button is None:
            self.navbar.set_trace_page_button()

    def remove_results_button(self):
        self.navbar.remove_results_button()

    def remove_trace_button(self):
        self.navbar.remove_trace_button()

    def initialise_results(self):
        self.current_frame = ResultsPage(self.master)

    def initialise_trace(self):
        self.current_frame = TracePage(self.master)

    @staticmethod
    def make_file():
        path = './model/trace.txt'
        if os.path.exists(path):
            os.remove(path)

        open(path, 'x').close()
