from model.knowledge_base import KnowledgeBase
from model.questions import Question
from model.rules.question_rules import rules_check
from model.rules.elimination_rules import elimination_update
from tkinter import *
from tkinter import ttk
from view.main_application import MainApp

user_kb = {}


def eliminate_studies(kb):
    size_kb = len(kb)
    i = 0
    # Iterating over all studies in the kb and eliminating those
    # which do not match
    while i < size_kb:
        elimination_update(kb[i], kb, user_kb)
        # After removal, the items are moved to a lower index in the list. 
        if len(kb) < size_kb:
            size_kb -= 1
            i -= 1
        i += 1


def forward_chaining(kb):
    queries = Question()
    question_list = queries.getQuestions()
    
    # fc while there are questions to ask
    while len(question_list) != 0:
        question = question_list[0]
        response = input(question + "\n")

        # Processing the user information and getting next questions
        rules_check(response, queries, kb, user_kb)
        queries.removeQuestion(question)
        question_list = queries.getQuestions()
        print("entering elim..")
        # Removing studies that don't match
        eliminate_studies(kb)
        if len(kb) == 0:
            print("No study requirements met.")
            break

    if len(kb) > 0:
        print("Requirements met for the following studies:")
        for study in kb:
            print(study['label'] + " at " + study['university'])


def main():
    root = Tk()
    root.title("Study Program Test")
    root.geometry('400x200')
    root.mainloop()
    
    kb = KnowledgeBase().kb
    forward_chaining(kb)


if __name__ == "__main__":
    main()
