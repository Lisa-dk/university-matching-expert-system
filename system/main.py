from model.knowledge_base import KnowledgeBase
from tkinter import *
from view.main_application import MainApp
from view.theme import Theme
import os

# bigger things todo:
# TODO: add descriptive disclaimers
# TODO: add scrollbar to trace page

# smaller things todo:
# TODO: consistent sizing of window
# TODO: look at theme
# TODO: button placements 
# TODO: clean up code from comments etc + apply same conventions everywhere (standard python convention)

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)


def main():
    root = Tk()
    root.title("University Matching Program for Turkish Students")
    #root.attributes("-fullscreen", True)

    width = 800
    height = 700
    x = root.winfo_screenwidth()/2 - width/2
    y = root.winfo_screenheight()/2 - height/2

    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.configure(bg=Theme.BG_COLOUR)
    MainApp(root)
    root.mainloop()
    remove_file('./model/disclaimers.txt')
    remove_file('./model/results.txt')
    remove_file('./model/trace.txt')


if __name__ == "__main__":
    main()
