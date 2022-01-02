from model.knowledge_base import KnowledgeBase
from tkinter import *
from view.main_application import MainApp
from view.theme import Theme


# TODO: consistent sizing of window
# DONE: making window appear in center -> DONE
# DONE: fix button placements input -> DONE
# DONE: make buttons change colour when going over them with the cursor -> DONE
# TODO: when input is number, make sure it is a number, and have the text field boxed.
# TODO: put the test in center, but results show at the top
# TODO: Separate pages for test results and home button and trace s.t. no information is lost unless new test is started
# TODO: add option to retake the test when results are shown or to show more information about the studies.
# TODO: if there are results, change 'take test' button at home page to 'retake test' button.
# TODO: Question types and input need to match + any possible error handling.
# TODO: save questions and answers to text file and results in separate text file


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
