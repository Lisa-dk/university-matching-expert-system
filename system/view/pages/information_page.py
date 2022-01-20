from tkinter import *
from PIL import ImageTk, Image
import os

from view.design.theme import Theme


class InformationPage:
    def __init__(self, main_app, master):
        self.button = None
        self.main_app = main_app
        self.master = master

        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.title_field = Text(self.frame, font=('Arial', 24, 'bold'), fg=Theme.INFO_HEADER, bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)
        self.welcome_field = Text(self.frame, font=('Arial', 18), fg=Theme.INFO_HEADER, bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)
        self.text_field = Text(self.frame, font=('Arial', 14), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)

        title = "University Matching Program"
        welcome = "Welcome to the study programme survey for universities in The Netherlands!"
        info = "This survey aims to recommend/match Turkish students with engineering study programmes at Dutch universities. " \
               "Be aware, however, that this survey only serves as a guide and does not take into consideration all specifications. " \
               "Because of this, you should check the requirements of the recommended study programmes as well."

        self.title_field.insert("1.0", title, CENTER)
        self.welcome_field.insert("1.0", welcome, CENTER)
        self.text_field.insert("1.0", info, CENTER)

        self.title_field.configure(state='disabled', width=80, height=2)
        self.welcome_field.configure(state='disabled', width=80, height=3)
        self.text_field.configure(state='disabled', width=100, height=10)

        self.canvas = Canvas(self.master, bg="white", width=350)
        self.canvas.pack(side=LEFT, fill=BOTH)

        img = Image.open("view/design/photo_information_page.jpg")
        zoom = 0.09
        pixels_x, pixels_y = tuple([int(zoom * x) for x in img.size])

        self.image = ImageTk.PhotoImage(img.resize((pixels_x, pixels_y))) 
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)

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
        Adds button to start the survey
        """
        self.button = Button(self.frame, text="Start Survey", 
                             font=('Arial', 15, 'bold'), 
                             padx=7, pady=5,
                             relief=RAISED,
                             bg=Theme.BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground=Theme.BUTTON_CLICK,
                             activeforeground='white',
                             bd=1, 
                             command=self.start_survey)
        self.button.pack(side=BOTTOM, pady=10)

    def make_retake_button(self):
        """
        Adds button to retake the survey
        """
        self.button = Button(self.frame, text="Retake Survey", 
                             font=('Arial', 15, 'bold'), 
                             padx=7, pady=5,
                             relief=RAISED,
                             bg=Theme.BUTTON_COLOUR,
                             fg=Theme.TEXT_COLOUR,
                             activebackground=Theme.BUTTON_CLICK,
                             activeforeground='white',
                             bd=1,
                             command=self.retake_survey)
        self.button.pack(side=BOTTOM, pady=10)

    def retake_survey(self):
        """
        Initialises the survey if retaking it
        """
        os.remove(self.path)
        self.main_app.remove_results_button()
        self.main_app.remove_trace_button()
        self.main_app.initialise_kb()
        self.start_survey()

    def start_survey(self):
        """
        Starts the survey
        """
        self.destroy()
        self.main_app.start_survey()

    def destroy(self):
        """
        Removes frame + items from main window
        :return:
        """
        self.button.destroy()
        self.text_field.destroy()
        self.canvas.destroy()
        self.frame.destroy()
