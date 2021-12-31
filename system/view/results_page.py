from view.theme import Theme
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import os


class ResultsPage:
    def __init__(self, master):
        self.number_results = None
        self.results_field = None
        self.master = master
        self.frame = Frame(self.master, bg="white", height=200, width=200)
        self.results = None
        self.load_results()
        self.display_results()
        self.frame.pack()

    def load_results(self):
        path = './model/results.txt'
        if os.path.exists(path):
            if os.stat(path).st_size == 0:
                self.results = "No requirements are met. No appropriate study programmes available."
            else:
                self.number_results = os.stat(path).st_size
                with open('./model/results.txt', 'r') as file:
                    self.results = "Requirements met for the following studies:\n\n"
                    for line in file:
                        result = line.split(',')
                        self.results += result[0] + " at" + result[1]
        else:
            messagebox.showerror("Error", "Something went wrong, please restart the program.")

    def display_results(self):
        self.results_field = Label(self.frame, textvariable=self.results, height=self.number_results, width=100,
                                   wraplength=500,
                                   justify=LEFT, font=Font(family="Arial"), fg=Theme.TEXT_COLOUR, bg=Theme.BG_COLOUR,
                                   bd=0)
        self.results_field.pack()
