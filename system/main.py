from model.knowledge_base import KnowledgeBase
from tkinter import *
from view.main_application import MainApp


# TODO: consistent sizing of window
# TODO: making window appear in center
# TODO: fix button placements and input font
# TODO: make buttons change colour when going over them with the cursor
# TODO: when input is number, make sure it is a number, and have the text field boxed.
# TODO: put the test in center, but results show at the top
# TODO: Separate pages for test results and home button and trace s.t. no information is lost unless new test is started
# TODO: add option to retake the test when results are shown or to show more information about the studies.
# TODO: if there are results, change 'take test' button at home page to 'retake test' button.
# TODO: Question types and input need to match + any possible error handling.


def main():
    root = Tk()
    root.title("Study Program Test")
    root.geometry("500x500")
    root.configure(bg="#1c4046")
    # MainApp(root, KnowledgeBase())
    MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
