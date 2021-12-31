from tkinter import LEFT, Label
from tkinter.font import Font

from model.knowledge_base import KnowledgeBase
from view.information_page import InformationPage
from view.nagivation_bar import NavBar
from view.question_field import QuestionField
from view.results_page import ResultsPage
from view.theme import Theme


class MainApp:
    # def __init__(self, master, kb):
    def __init__(self, master):
        self.results_page = None
        self.master = master
        self.start_page = None
        self.question_field = None
        # self.kb = kb
        self.kb = None

        self.navbar = NavBar(self.master, self)
        self.initialise()

    def initialise(self):
        self.kb = KnowledgeBase()
        self.start_page = InformationPage(self, self.master)

    def start_test(self):
        self.start_page = None
        self.question_field = QuestionField(self.master, self.kb, self)

    # not sure where to do this
    def add_test_page_button(self):
        if self.navbar.results_page_button is None:
            self.navbar.set_results_page_button()

    def show_results(self):
        print('reached main show reuslts')
        self.results_page = ResultsPage(self.master)

