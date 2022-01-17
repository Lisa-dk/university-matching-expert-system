from tkinter import *
import os

# from model.knowledge_base import KnowledgeBase
from view.main_application import MainApp
from view.theme import Theme

# smaller things to-do:
# DONE: consistent sizing of window
# DONE: look at theme
# DONE: button placements
# TODO: clean up code from comments etc + apply same conventions everywhere (standard python convention)
# TODO: Remove print statements to the terminal --> NOTE: I did not delete all of it, should we?
# TODO: Previous Button
# TODO: fit frame to 'Do you follow the following IB courses?" question (since now HL SL standard form info is added)
# DONE: add links
# DONE: Add Vrije University
# TODO: check disclaimer texts? -> NOTE: I corrected the one for English
# DONE: Size scrollbar frame multiple-choice
# DONE: Placement frame results
# DONE: Size scrollbar frame trace
# DONE: Placement frame trace


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)


def main():
    root = Tk()
    root.title("University Matching Program for Turkish Students")

    width = 750
    height = 600
    x = root.winfo_screenwidth()/2 - width/2
    y = root.winfo_screenheight()/2 - height/2

    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(height=False, width=False)
    root.configure(bg=Theme.BG_COLOUR)
    MainApp(root)
    root.mainloop()
    remove_file('./model/disclaimers.txt')
    remove_file('./model/results.txt')
    remove_file('./model/trace.txt')


if __name__ == "__main__":
    main()
