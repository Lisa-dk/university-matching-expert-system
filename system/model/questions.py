from enum import Enum

class QuestionType(Enum):
    SELECT = 1
    MULTI_SELECT = 2

class Question():
    def __init__(self):
        self.questions = ["----> What is your highschool diploma?"]

    def getQuestions(self):
        return self.questions
    
    def getCurrentQuestion(self):
        return self.questions[0]

    def addQuestion(self, question):
        self.questions.append(question)

    def removeQuestion(self):
        self.questions.pop(0)

    def clearQuestion(self):
        self.questions.clear()

    def getQuestionListLen(self):
        return len(self.questions)

    def endProgram(self):
        return 'end'
    
