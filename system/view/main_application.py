from model.knowledge_base import KnowledgeBase
from view.information_page import InformationPage
from view.nagivation_bar import NavBar
from view.question_field import QuestionField


class MainApp:
    def __init__(self, master):
        self.master = master
        self.start_page = None
        self.question_field = None
        self.kb = None

        self.navbar = NavBar(self.master, self)
        self.initialise_kb()
        self.initialise_home()

    def initialise_kb(self):
        self.kb = KnowledgeBase()

    def initialise_home(self):
        self.start_page = InformationPage(self, self.master)

    def start_test(self):
        self.start_page = None
        self.question_field = QuestionField(self.master, self.kb)
    
    def add_test_page_button(self):
        if self.navbar.results_page_button is None:
            self.navbar.set_results_page_button()
