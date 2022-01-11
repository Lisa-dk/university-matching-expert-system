from tkinter.font import Font
from tkinter import *
from view.theme import Theme
from PIL import ImageTk, Image

import os

class InformationPage:
    def __init__(self, main_app, master):
        self.button = None
        self.main_app = main_app
        self.master = master
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.title_field = Text(self.frame, font=('Arial', 30, 'bold'), fg="blue", bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)
        self.text_field = Text(self.frame, font=('Arial', 17, 'italic'), fg="black", bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)
        welcome = "Welcome to the study programme test!\n\n"
        info = "This test aims to recommend/match Turkish students with engineering study programmes at Dutch universities.\nBe aware, however, that this test only serves as a guide and does not take into consideration all specification.\nBecause of this, you should check the requirements of the recommended study programmes as well."
        self.title_field.insert("1.0", welcome, CENTER)
        self.text_field.insert("1.0", info, CENTER)
        self.title_field.configure(state='disabled', width=80, height=3)
        self.text_field.configure(state='disabled', width=80, height=10)

        self.canvas = Canvas(self.master, bg="white", width=420)
        self.canvas.pack(side=LEFT, fill=BOTH)
        self.image = ImageTk.PhotoImage(Image.open("view/pages/student_photo.jpg"))
        self.canvas.create_image(0,0, 
                                anchor=NW, 
                                image=self.image)
        self.canvas.create_text(3,612, text="https://www.istockphoto.com/tr/foto%C4%9Fraf/s%C4%B1n%C4%B1flar-aras%C4%B1nda-koridorda-%C3%B6%C4%9Frenciler-gm1202242519-345072828",
                                font=("Arial", 10),
                                fill="dark blue",
                                anchor=NW,
                                state=DISABLED,
                                width=420)

        self.path = './model/results.txt'
        if os.path.exists(self.path):
            self.make_retake_button()
        else:
            self.make_start_button()

        self.title_field.pack(side=TOP)
        self.text_field.pack()
        self.button.pack(side=BOTTOM, pady=15)
        self.frame.pack()
        
    def make_start_button(self):
        """
        Adds button to start the test
        """
        self.button = Button(self.frame, text="Start Test", 
                             font=('Arial', 15, 'bold'), 
                             padx=7,
                             pady=7,
                             relief=RAISED,
                             bg=Theme.BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground="green",
                             activeforeground='white',
                             bd=1, 
                             command=self.start_test)

    def make_retake_button(self, ):
        """
        Adds button to retake the test
        """
        self.button = Button(self.frame, text="Retake Test", 
                             font=('Arial', 15, 'bold'), 
                             padx=7,
                             pady=7,
                             relief=RAISED,
                             bg=Theme.BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground="green",
                             activeforeground='white',
                             bd=1, 
                             command=self.retake_test)
                             

    def retake_test(self):
        """
        Initialises the test if retaking it
        """
        os.remove(self.path)
        self.main_app.remove_results_button()
        self.main_app.remove_trace_button()
        self.main_app.initialise_kb()
        self.start_test()

    def start_test(self):
        """
        Starts the test
        """
        self.destroy()
        self.main_app.start_test()

    def destroy(self):
        """
        Removes frame + items from main window
        :return:
        """
        self.button.destroy()
        self.text_field.destroy()
        self.canvas.destroy()
        self.frame.destroy()
