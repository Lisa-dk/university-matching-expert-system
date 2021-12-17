from tkinter import *

class QuestionField():
    def __init__(self, master, inference_engine):
        self.master = master
        self.inference_engine = inference_engine
        self.addTextField(self.master)
        self.setText(self.inference_engine.getCurrentQuestion())
        self.inputField = InputFields(self.master, self.inference_engine)
        self.addSaveButton(self.master)
    
    def addTextField(self, frame):
        self.textField = Text(frame, height=5, width=100)
        self.textField.pack()

    def setText(self, text):
        self.textField.insert(END, text)
    
    def addSaveButton(self, frame):
        self.button = Button(frame, height=1, width=10, text="Next", 
                            command=lambda: self.setInput())
        self.button.pack()
    
    def setInput(self):
        inputTextField = self.inputField.inputText
        input = inputTextField.get("1.0", "end-1c")
        self.inference_engine.setRespone(input)
    
    def getInput(self):
        return self.input

class InputFields():
    def __init__(self, master, inference_engine):
        self.master = master
        self.inference_engine = inference_engine
        self.addInputTextField(self.master)
    
    def addInputTextField(self, frame):
        self.inputText = Text(frame, height=3, width=10)
        self.inputText.pack()