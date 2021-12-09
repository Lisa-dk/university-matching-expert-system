class Question():
    def __init__(self):
        self.questions = ["What subjects did you take?"]

    def getQuestions(self):
        return self.questions

    def addQuestion(self, question):
        self.questions.append(question)

    def removeQuestion(self, question):
        self.questions.remove(question)

