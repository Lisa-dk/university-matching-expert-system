from tkinter import LEFT, Label
from tkinter.font import Font

from model.knowledge_base import KnowledgeBase
from view.information_page import InformationPage
from view.nagivation_bar import NavBar
from view.question_field import QuestionField
from view.results_page import ResultsPage
from view.theme import Theme


class MainApp:
    def __init__(self, master):
        self.results_page = None
        self.master = master
        self.start_page = None
        self.question_field = None
        self.kb = None
        self.currentFrame = None

        self.navbar = NavBar(self.master, self)
        self.initialise_kb()
        self.initialise_home()

    def initialise_kb(self):
        self.kb = KnowledgeBase()

    def initialise_home(self):
        if not type(self.currentFrame) == InformationPage:
            self.start_page = InformationPage(self, self.master)
            self.currentFrame = self.start_page

    def start_test(self):
        if not type(self.currentFrame) == QuestionField:
            self.start_page = None
            self.question_field = QuestionField(self.master, self.kb, self)
            self.currentFrame = self.question_field

    def add_test_page_button(self):
        if self.navbar.results_page_button is None:
            self.navbar.set_results_page_button()

    def show_results(self):
        if not type(self.currentFrame) == ResultsPage:
            print('reached main show reuslts')
            self.results_page = ResultsPage(self.master)
            self.currentFrame = self.results_page

