from model.knowledge_base import KnowledgeBase
from tkinter import *
from tkinter import ttk
from view.main_application import MainApp


# TODO: Fc is only executed after the interface has been closed. We need to find a way to merge the two
# such that we dont make a new window all the time and also such that fc is 'paused' when waiting for a response
# and that it doesnt just keep repeating with the existing response.
def main():
    root = Tk()
    root.title("Study Program Test")
    root.geometry("500x500")
    root.configure(bg="#1c4046")
    MainApp(root, KnowledgeBase())
    root.mainloop()


if __name__ == "__main__":
    main()
