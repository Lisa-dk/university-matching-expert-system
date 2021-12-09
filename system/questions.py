class Question():
    def __init__(self) -> None:
        self.questions = ["What subjects did you take?"]

    def addQuestion(self, question):
        self.questions.append(question)

    def removeQuestion(self, question):
        self.questions.remove(question)

