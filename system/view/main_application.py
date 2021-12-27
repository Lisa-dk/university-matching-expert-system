from tkinter.font import Font
from tkinter import *
from view.nagivation_bar import NavBar
from view.question_field import QuestionField


class InformationPage:
    def __init__(self, main_app, master):
        self.main_app = main_app
        self.master = master
        self.frame = Frame(self.master, bg="#1c4046")
        self.text_field = Text(self.frame, font=Font(family="Arial"), fg="white", bg="#1c4046", bd=0)
        info = "\nWelcome to the study programme test!\n" \
               "This test aims to recommend/match Turkish students with enginering study programmes at Dutch " \
               "universities. Be aware, however, that not all requirements are included and you should check the " \
               "requirements of the recommended universities as well."
        self.text_field.insert(END, info)
        self.text_field.configure(state='disabled', width=53, height=8)
        self.button = Button(self.frame, text="Start Test", bg="#768c90", bd=1, command=self.start_test)

        self.text_field.pack()
        self.button.pack()
        self.frame.pack()

    def start_test(self):
        self.button.destroy()
        self.text_field.destroy()
        self.frame.destroy()
        self.main_app.start_test()


class MainApp:
    def __init__(self, master, kb):
        self.question_field = None
        self.master = master
        self.kb = kb

        self.navbar = NavBar(self.master)
        self.frame = Frame(self.master, bg="white")
        self.start_page = InformationPage(self, self.master)

    def start_test(self):
        self.start_page = None
        self.question_field = QuestionField(self.master, self.kb)

