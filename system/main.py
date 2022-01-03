from model.knowledge_base import KnowledgeBase
from tkinter import *
from view.main_application import MainApp
from view.theme import Theme


# TODO: consistent sizing of window
# DONE: making window appear in center -> DONE
# DONE: fix button placements input -> DONE
# DONE: make buttons change colour when going over them with the cursor -> DONE
# TODO: when input is number, make sure it is a number
# DONE:have the text field boxed.
# DONE: Results page
# TODO: trace page
# DONE: retake/take test in home page
# TODO: add option to show more information about the studies.
# TODO: Question types and input need to match + any possible error handling.
# TODO: save questions and answers to text file
# Done: put results in separate text file


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
