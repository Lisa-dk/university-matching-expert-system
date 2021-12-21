from tkinter import *
from control.next_button import loadNewQuestion
from model.questions import Question

class QuestionField():
    def __init__(self, master, kbClass):
        self.master = master
        self.questionClass = Question()
        self.question = self.questionClass.getQuestions()[0]
        self.kbClass = kbClass

        self.addTextField(self.master)
        self.addText(self.question)

        self.inputField = InputFields(self.master)

        self.addSaveButton(self.master)
    

    def addTextField(self, frame):
        self.textField = Text(frame, height=5, width=100)
        self.textField.pack()


    def addText(self, text):
        self.textField.insert(END, text)
    

    def addSaveButton(self, frame):
        self.button = Button(frame, height=1, width=10, text="Next", 
                            command=lambda: loadNewQuestion(self, self.kbClass, self.questionClass, self.question, self.inputField))
        self.button.pack()

    # updates the question and input text fields
    def update(self, EMPTY):
        self.textField.delete("1.0", "end-1c")
        self.inputField.inputText.delete("1.0", "end-1c")

        if len(self.kbClass.kb) == 0:
                self.addText("No requirements are met. No appropriate study programmes available.")

        if not EMPTY and len(self.kbClass.kb) > 0:
            self.question = self.questionClass.getQuestions()[0]
            self.addText(self.question)
        else:
            self.inputField.inputText.destroy()
            self.button.destroy()
            self.give_results()

        
    # prints the studies for which the requirements are met.
    def give_results(self):
        results = "Requirements met for the following studies:\n"
        if len(self.kbClass.kb) > 0:
            for study in self.kbClass.kb:
                results += study['label'] + " at " + study['university'] + "\n"
        self.addText(results)
            

class InputFields():
    def __init__(self, master):
        self.master = master
        self.addInputTextField(self.master)
    
    def addInputTextField(self, frame):
        self.inputText = Text(frame, height=3, width=10)
        self.inputText.pack()
    
