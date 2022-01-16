# from tkinter.font import Font
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
        self.title_field = Text(self.frame, font=('Arial', 24, 'bold'), fg=Theme.INFO_HEADER, bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)
        self.welcome_field = Text(self.frame, font=('Arial', 18), fg=Theme.INFO_HEADER, bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)
        self.text_field = Text(self.frame, font=('Arial', 14), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)

        title = "International University Matching Program"
        welcome = "Welcome to the study programme test for universities in The Netherlands!"
        info = "This test aims to recommend/match Turkish students with engineering study programmes at Dutch universities. " \
               "Be aware, however, that this test only serves as a guide and does not take into consideration all specification. " \
               "Because of this, you should check the requirements of the recommended study programmes as well."

        self.title_field.insert("1.0", title, CENTER)
        self.welcome_field.insert("1.0", welcome, CENTER)
        self.text_field.insert("1.0", info, CENTER)

        self.title_field.configure(state='disabled', width=80, height=2)
        self.welcome_field.configure(state='disabled', width=80, height=3)
        self.text_field.configure(state='disabled', width=100, height=10)

        self.canvas = Canvas(self.master, bg="white", width=350)
        self.canvas.pack(side=LEFT, fill=BOTH)

        img = Image.open("view/pages/photo_information_page.jpg")
        zoom = 0.09
        pixels_x, pixels_y = tuple([int(zoom * x) for x in img.size])

        self.image = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y))) 
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        # self.canvas.create_text(3, 545,
        #                         text="https://www.pexels.com/photo/friends-sitting-in-the-library-8199567/",
        #                         font=("Arial", 10),
        #                         fill="dark blue",
        #                         anchor=NW,
        #                         state=DISABLED,
        #                         width=330)

        self.path = './model/trace.txt'
        if os.path.exists(self.path):
            self.make_retake_button()
        else:
            self.make_start_button()

        self.title_field.pack(anchor='w', pady=10, fill=X)
        self.welcome_field.pack(anchor='w', pady=15, fill=X)
        self.text_field.pack(anchor='w', fill=X)
        self.frame.pack(anchor='e', padx=10, pady=0)
        
    def make_start_button(self):
        """
        Adds button to start the test
        """
        self.button = Button(self.frame, text="Start Test", 
                             font=('Arial', 15, 'bold'), 
                             padx=7, pady=5,
                             relief=RAISED,
                             bg=Theme.BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground=Theme.BUTTON_CLICK,
                             activeforeground='white',
                             bd=1, 
                             command=self.start_test)
        self.button.pack(side=BOTTOM, pady=10)

    def make_retake_button(self):
        """
        Adds button to retake the test
        """
        self.button = Button(self.frame, text="Retake Test", 
                             font=('Arial', 15, 'bold'), 
                             padx=7, pady=5,
                             relief=RAISED,
                             bg=Theme.BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground=Theme.BUTTON_CLICK,
                             activeforeground='white',
                             bd=1,
                             command=self.retake_test)
        self.button.pack(side=BOTTOM, pady=10)

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
