from tkinter import *
from tkinter import ttk
from view.nagivation_bar import NavBar

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

        
class MainApp():
    def __init__(self, master, inference_engine):
        print("hello")
        self.master = master
        self.inerence_engine = inference_engine
        self.frame = Frame(self.master, bg="white")
        self.navbar = NavBar(self.master)
        
        self.frame.pack(side="top", fill='x', ipadx=10, ipady=10)
        intro_lbl = Label(self.frame, text="Welcome to the Study Program test for Turkish students \n"
                                        "who are interested in studying in The Netherlands.", font=("Arial", 12))
        intro_lbl.grid(column=0, row=0)
        self.questionField = QuestionField(self.master, self.inerence_engine)


    def onExit(self):
        self.frame.destroy()
        self.quit()