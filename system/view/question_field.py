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
        self.setText(self.question)

        self.inputField = InputFields(self.master)

        self.addSaveButton(self.master)
    
    def addTextField(self, frame):
        self.textField = Text(frame, height=5, width=100)
        self.textField.pack()

    def setText(self, text):
        self.textField.insert(END, text)
    
    def addSaveButton(self, frame):
        self.button = Button(frame, height=1, width=10, text="Next", 
                            command=lambda: loadNewQuestion(self, self.kbClass, self.questionClass, self.question, self.inputField))
        self.button.pack()

    def update(self, EMPTY):
        self.textField.delete("1.0", "end-1c")

        if len(self.kbClass.kb) == 0:
                self.setText("No requirements are met. No appropriate study programmes available.")

        if not EMPTY and len(self.kbClass.kb) > 0:
            self.question = self.questionClass.getQuestions()[0]
            self.setText(self.question)
        else:
            self.inputField.inputText.destroy()
            self.button.destroy()
            self.give_results()
        
        self.inputField.inputText.delete("1.0", "end-1c")
    
    def give_results(self):
        if len(self.kbClass.kb) > 0:
            self.setText("Requirements met for the following studies:\n")
            for study in self.kb:
                    self.setText(study['label'] + " at " + study['university'] + "\n")
            

class InputFields():
    def __init__(self, master):
        self.master = master
        self.addInputTextField(self.master)
    
    def addInputTextField(self, frame):
        self.inputText = Text(frame, height=3, width=10)
        self.inputText.pack()
    
