from model.knowledge_base import KnowledgeBase
from model.InferenceEngine import InferenceEngine
from tkinter import *
from tkinter import ttk
from view.main_application import MainApp


#TODO: Fc is only executed after the interface has been closed. We need to find a way to merge the two
# such that we dont make a new window all the time and also such that fc is 'paused' when waiting for a response
# and that it doesnt just keep repeating with the existing response.
def main():
    kb = KnowledgeBase().kb
    fc = InferenceEngine(kb)

    '''
    root = Tk()
    root.title("Study Program Test")
    root.minsize(500, 500)
    MainApp(root, fc)
    root.mainloop()
    '''

    fc.forward_chaining()


if __name__ == "__main__":
    main()
