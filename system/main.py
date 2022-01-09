from model.knowledge_base import KnowledgeBase
from tkinter import *
from view.main_application import MainApp
from view.theme import Theme


# bigger things todo:
#TODO: add trace
#       -> add advise/disclaimer/explanations to trace?? (im not sure when we should add the explanations but the trace seems like a good place)
#DONE   -> save questions and answers to text file + load (like results)
# TODO: fix grade processing for english tests
# TODO: add descriptive disclaimers
# DONE: list implementation to replace regex
# TODO: comment code (likely when finalised)
# TODO: fix scrollbar
# TODO: add scrollbar to trace page


# smaller things todo:
# TODO: consistent sizing of window
# TODO: when input is number, make sure it is a number
# TODO: implement grade ranges (for both subjects (done) and english)
# TODO: add option to show more information about the studies. (not necessary)
# TODO: Question Types and input need to match + any possible error handling.
# TODO: look at theme
# TODO: button placements 
# TODO: clean up code from comments etc + apply same conventions everywhere (standard python convention)


def main():
    root = Tk()
    root.title("Study Program Test")

    width = 500
    height = 500
    x = root.winfo_screenwidth()/2 - width/2
    y = root.winfo_screenheight()/2 - height/2

    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.configure(bg=Theme.BG_COLOUR)
    MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
