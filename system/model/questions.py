from enum import Enum

class QuestionType(Enum):
    SELECT = 1
    MULTI_SELECT = 2

class Question():
    def __init__(self):
        self.questions = ["----> What is your highschool diploma?"]

    def getQuestions(self):
        return self.questions

    def addQuestion(self, question):
        self.questions.append(question)

    def removeQuestion(self, question):
        self.questions.remove(question)
