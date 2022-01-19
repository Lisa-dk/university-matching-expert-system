from tkinter import messagebox
from view.theme import Theme
from tkinter import *
# from tkinter.font import Font
import os


def load_disclaimers():
    """
    Loads disclaimers from text file
    """
    path = './model/disclaimers.txt'
    if os.path.exists(path):
        if os.stat(path).st_size == 0:
            return "No requirements are met.\nNo appropriate study programmes available."
        else:
            with open('./model/disclaimers.txt', 'r') as file:
                disclaimers = ''
                for line in file:
                    disclaimers += line
                file.close()
                return disclaimers
    else:
        messagebox.showerror("Error", "Something went wrong, please restart the program.")


def load_results():
    """
    Loads results from text file
    :return: string with recommended study programmes
    """
    path = './model/results.txt'
    if os.path.exists(path):
        if os.stat(path).st_size == 0:
            if os.path.exists('./model/disclaimers.txt'):
                return load_disclaimers()
            else:
                return "No requirements are met.\nNo appropriate study programmes available."
        else:
            with open('./model/results.txt', 'r') as file:
                results = "Requirements met for the following studies:\n\n"
                for line in file:
                    result = line.split(',')
                    if len(result) == 3:
                        results += "- " + result[0] + " at" + result[1] + "\n" + result[2] + "\n"
                    else:
                        results += "- " + result[0] + " at" + result[1]  + "\n" + result[2] + "\n"
                file.close()
                return results
    else:
        messagebox.showerror("Error", "Something went wrong, please restart the program.")


class ResultsPage:
    def __init__(self, master):
        self.master = master
        self.number_results = None
        self.results_field = None
        self.disclaimer_field = None
        self.disclaimer_header = None

        #self.frame = Frame(self.master, bg=Theme.BG_COLOUR, width=750, height=600)
        # self.frame.pack()
        self.frame = Frame(self.master, bg=Theme.BG_COLOUR, width=750, height=600)
        self.scrollbar = Scrollbar(self.frame, orient="vertical", bg=Theme.BG_COLOUR)
        self.scrollbar.pack(fill='y', side='right', pady=10)

        self.display_results()

        self.scrollbar.config(command=self.results_field.yview)
        self.frame.pack(anchor='center', ipady=10, ipadx=10)


    def display_results(self):
        """
        Shows the results in the frame
        """
        results = load_results()
        #print('results:\n', results)

        self.results_field = Text(self.frame, yscrollcommand=self.scrollbar.set, font=('Arial', 16), fg=Theme.TEXT_COLOUR,
                                  bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0)

        self.results_field.insert("1.0", results, CENTER)

        self.results_field.configure(state='disabled', width=200, height=25)

        self.results_field.pack(anchor='w', fill=X)
        self.frame.pack(anchor='e', padx=10, pady=10)

    def destroy(self):
        """
        Removes the frame + its items
        """
        if self.disclaimer_field is not None:
            self.disclaimer_header.destroy()
            self.disclaimer_field.destroy()
        self.results_field.destroy()
        self.frame.destroy()
        self.scrollbar.destroy()
