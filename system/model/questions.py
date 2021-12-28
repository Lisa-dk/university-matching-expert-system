from enum import Enum


class QuestionType(Enum):
    SELECT = 1
    MULTI_SELECT = 2


class Question:
    def __init__(self):
        self.questions = ["----> What is your high school diploma?"]

    def get_questions(self):
        return self.questions

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        self.questions.remove(question)
