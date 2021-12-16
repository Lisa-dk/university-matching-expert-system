# from knowledge_base import KnowledgeBase
# from questions import Question
# from rules.question_rules import rules_check
# from rules.elimination_rules import elimination_update

from tkinter import *
from tkinter import ttk


root = Tk()

root.title("Study Program Test")
root.geometry('400x200')


def start():
    start_frame = Frame(root)
    start_frame.pack()

    intro_lbl = Label(start_frame, text="Welcome to the Study Program test for Turkish students \n"
                                        "who are interested in studying in The Netherlands.", font=("Arial", 12))
    intro_lbl.grid(column=0, row=0)

    def question1():
        start_frame.destroy()

        frame1 = Frame(root)
        frame1.pack()

        diploma_lbl = Label(frame1, text="What is your high school diploma?", font=("Arial", 12))
        diploma_lbl.grid(column=0, row=0)

        diploma = ttk.Combobox(frame1, state="readonly")

        diploma['values'] = ("Regular Lise Diploma", "AP", "IB", "Label France Education", "British GCE A Levels")
        diploma.current(0)  # set the selected item
        diploma.grid(column=0, row=1)

        def question2():
            d = diploma.get()
            frame1.destroy()
            frame2 = Frame(root)
            frame2.pack()

            lbl = Label(frame2, text="{} is selected!".format(d))
            lbl.grid(column=0, row=0)

            def restart():
                frame2.destroy()
                start()

            restart_btn = Button(frame2, text="Restart", command=restart)
            restart_btn.grid(column=0, row=1)

        confirm_btn = Button(frame1, text="Select", command=question2)
        confirm_btn.grid(column=1, row=1)
        # confirm_btn.pack()

    start_btn = Button(start_frame, text="Start", command=question1, font=("Arial", 12), bg="orange", fg="white")
    start_btn.grid(column=0, row=1)


start()

root.mainloop()
