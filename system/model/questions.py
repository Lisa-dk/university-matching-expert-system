from enum import Enum


class QuestionType(Enum):
    SELECT = 1
    MULTI_SELECT = 2
    TEXT_FIELD = 3


class Question:
    def __init__(self):
        self.questions = ["---> Do you know what you want to study?"]
        # self.questions = [("Do you know what you want to study?", QuestionType.SELECT, ['yes', 'no'])]
        # self.questions = ["----> What is your high school diploma?"]

    def get_questions(self):
        return self.questions

    def getCurrentQuestion(self):
        return self.questions[0]

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        self.questions.remove(question)
        # self.questions.pop(0)

    def clearQuestion(self):
        self.questions.clear()

    def getQuestionListLen(self):
        return len(self.questions)