from tkinter import messagebox
from view.theme import Theme
from tkinter import *
from tkinter.font import Font
import os


class ResultsPage:
    def __init__(self, master):
        self.master = master
        self.number_results = None
        self.results_field = None
        self.disclaimer_field = None
        self.disclaimer_header = None

        self.frame = Frame(self.master, bg=Theme.BG_COLOUR)
        self.frame.pack()

        self.display_results()
        self.load_disclaimers()

    def load_results(self):
        """
        Loads results from text file
        :return: string with recommended study programmes
        """
        path = './model/results.txt'
        if os.path.exists(path):
            if os.stat(path).st_size == 0:
                return "No requirements are met.\nNo appropriate study programmes available."
            else:
                with open('./model/results.txt', 'r') as file:
                    results = "Requirements met for the following studies:\n\n"
                    for line in file:
                        result = line.split(',')
                        results += result[0] + " at" + result[1]
                    file.close()
                    return results
        else:
            messagebox.showerror("Error", "Something went wrong, please restart the program.")

    def load_disclaimers(self):
        """
        Loads disclaimers from text file
        """
        path = './model/disclaimers.txt'
        if os.path.exists(path):
            if os.stat(path).st_size == 0:
                pass
            else:
                with open('./model/disclaimers.txt', 'r') as file:
                    disclaimers = ''
                    for line in file:
                        disclaimers += line
                    file.close()
                    self.display_disclaimers(disclaimers)
        else:
            messagebox.showerror("Error", "Something went wrong, please restart the program.")


    def display_results(self):
        """
        Shows the results in the frame
        """
        results = self.load_results()
        print('results:\n', results)
        self.results_field = Label(self.frame, text=results, width=200,
                                   wraplength=800, justify=LEFT, font=('Arial', 20), fg=Theme.RESULT_TEXT,
                                   bg=Theme.BG_COLOUR, bd=0)
        self.results_field.pack(side=TOP, ipady=10)
    

    def display_disclaimers(self, disclaimers):
        """
        Shows additional short explanation for the results.
        """
        self.disclaimer_header = Label(self.frame, text="\nShort explanation:\n", width=100,
                                   wraplength=500, justify=LEFT, font=("Arial bold", 20, 'underline'), fg=Theme.DISCLAIMER_HEADER,
                                   bg=Theme.BG_COLOUR, bd=0)
        self.disclaimer_header.pack(side=TOP, anchor=W)
        self.disclaimer_field = Label(self.frame, text=disclaimers, width=100,
                                   wraplength=500, justify=LEFT, font=('Arial', 17), fg=Theme.TEXT_COLOUR,
                                   bg=Theme.BG_COLOUR, bd=0)
        self.disclaimer_field.pack(side=TOP)

    def destroy(self):
        """
        Removes the frame + its items
        """
        if self.disclaimer_field is not None:
            self.disclaimer_header.destroy()
            self.disclaimer_field.destroy()
        self.results_field.destroy()
        self.frame.destroy()
