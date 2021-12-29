from model.knowledge_base import KnowledgeBase
from view.information_page import InformationPage
from view.nagivation_bar import NavBar
from view.question_field import QuestionField


class MainApp:
    # def __init__(self, master, kb):
    def __init__(self, master):
        self.master = master
        self.start_page = None
        self.question_field = None
        self.kb = None

        self.navbar = NavBar(self.master, self)
        self.initialise()

    def initialise(self):
        self.kb = KnowledgeBase()
        self.start_page = InformationPage(self, self.master)

    def start_test(self):
        self.start_page = None
        self.question_field = QuestionField(self.master, self.kb)
