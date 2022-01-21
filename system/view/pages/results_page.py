from tkinter import *
from tkinter import messagebox
import os

from control.tkHyperlinkManager import HyperlinkManager
from view.design.theme import Theme


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


class ResultsPage:
    def __init__(self, master):
        self.master = master
        self.number_results = None
        self.results_field = None
        self.hyperlink = None

        self.frame = Frame(self.master, bg=Theme.BG_COLOUR, width=750, height=600)
        self.scrollbar = Scrollbar(self.frame, orient="vertical", bg=Theme.BG_COLOUR)
        self.scrollbar.pack(fill='y', side='right', pady=10)

        self.display_results()

        self.scrollbar.config(command=self.results_field.yview)
        self.frame.pack(anchor='center', ipady=10, ipadx=10)

    def load_results(self):
        """
        Loads results from text file
        :return: string with recommended study programmes
        """
        path = './model/results.txt'
        if os.path.exists(path):
            if os.stat(path).st_size == 0:
                if os.path.exists('./model/disclaimers.txt'):
                    text = load_disclaimers()
                    self.results_field.insert("1.0", text, CENTER)
                else:
                    text = "No requirements are met.\nNo appropriate study programmes available."
                    self.results_field.insert("1.0", text, CENTER)
            else:
                with open('./model/results.txt', 'r') as file:
                    header = "Requirements met for the following studies:"
                    self.results_field.insert(END, header)
                    header_end = self.results_field.index("end")
                    self.results_field.insert(END, "\n\n")

                    self.results_field.tag_add("header", "1.0", header_end)
                    self.results_field.tag_config("header", font=('Arial', 18, 'bold'), foreground=Theme.TITLE)

                    x = -1
                    for line in file:
                        x += 1
                        result = line.split(', ')
                        if len(result) == 3:
                            study_text = "- " + result[0] + " at " + result[1]
                            self.results_field.insert(END, study_text)
                            self.results_field.insert(END, "\n")

                            start = self.results_field.index("end")
                            url = result[2]
                            self.results_field.insert(END, url, self.hyperlink.add(url))
                            end = self.results_field.index("end")

                            tag_label = "url" + str(x)
                            self.results_field.tag_add(tag_label, start, end)
                            self.results_field.tag_config("start", font=('Arial', 16, 'underline'), foreground="blue")
                            self.results_field.insert(END, "\n")
                    file.close()
        else:
            messagebox.showerror("Error", "Something went wrong, please restart the program.")

    def display_results(self):
        """
        Shows the results in the frame
        """
        self.results_field = Text(self.frame, yscrollcommand=self.scrollbar.set, font=('Arial', 16),
                                  fg=Theme.TEXT_COLOUR,
                                  bg=Theme.BG_COLOUR, bd=0, wrap='word', relief=FLAT, border=0, cursor="arrow")
        self.hyperlink = HyperlinkManager(self.results_field)

        self.load_results()

        self.results_field.configure(state='disabled', width=200, height=25)
        self.results_field.pack(anchor='e', fill=X)

        self.frame.pack(anchor='e', padx=10, pady=10)

    def destroy(self):
        """
        Removes the frame + its items
        """
        self.results_field.destroy()
        self.hyperlink.reset()
        self.frame.destroy()
        self.scrollbar.destroy()
