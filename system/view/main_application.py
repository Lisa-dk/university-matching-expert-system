from model.knowledge_base import KnowledgeBase
from view.information_page import InformationPage
from view.nagivation_bar import NavBar
from view.question_field import QuestionField
from view.results_page import ResultsPage
import os

from view.trace_page import TracePage


class MainApp:
    def __init__(self, master):
        self.master = master
        self.kb = None
        self.current_frame = None

        self.navbar = NavBar(self.master, self)
        self.initialise_kb()
        self.initialise_home()
        self.make_file()

    def initialise_kb(self):
        self.kb = KnowledgeBase()

    def initialise_home(self):
        self.current_frame = InformationPage(self, self.master)

    def start_test(self):
        self.current_frame = QuestionField(self.master, self.kb, self)
    
    def add_results_page_button(self):
        if self.navbar.results_page_button is None:
            self.navbar.set_results_page_button()

    def add_trace_page_button(self):
        if self.navbar.trace_page_button is None:
            self.navbar.set_trace_page_button()

    def remove_results_button(self):
        self.navbar.remove_results_button()

    def initialise_results(self):
        self.current_frame = ResultsPage(self.master)

    def initialise_trace(self):
        self.current_frame = TracePage(self.master)

    def make_file(self):
        path = './model/trace.txt'
        if os.path.exists(path):
            os.remove(path)

        open(path, 'x').close()
