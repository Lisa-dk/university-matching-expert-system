from tkinter import *
import os

from view.main_application import MainApp
from view.theme import Theme


# smaller things to-do:
# TODO: clean up code from comments etc + apply same conventions everywhere (standard python convention)
# TODO: Previous Button
# TODO: check disclaimer texts? -> NOTE: I corrected the one for English


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
