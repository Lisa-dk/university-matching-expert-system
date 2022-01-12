from model.rules.elimination_rules import elimination_update
from model.rules.user_rules import edit_user_kb
from tkinter import messagebox
import os


def load_new_question(question_field, kb_class, question_class, question, input_field):
    """
    Acts as the inference engine. Updates the question, trace, processes the user input, and eliminates studies while
    there are still questions to be asked.
    :param question_field: class containing the input options
    :param kb_class: class containing the kb and user kb
    :param question_class: class containing the questions
    :param question: the current question
    :param input_field: field containg the user input
    """
    # obtaining the input
    answer = input_field.get_chosen_option()
    if answer == "" or (type(answer) == list and len(answer) == 0):
        # Stay with current question
        messagebox.showwarning("Warning", "Please select an option to continue")
    else:
        # Checking with the rules and removing the question
        edit_user_kb(answer, question_class, question_field.disclaimer, kb_class.kb, kb_class.user_kb,
                     question_field.visited)
        question_class.remove_question(question)
        elim_studies = eliminate_studies(kb_class, question_field.visited)
        # Adding to the trace
        save_trace(question[0], answer, elim_studies)

        # Noting whether there are questions left.
        empty = 0 if len(question_class.get_questions()) > 0 else 1
        question_field.update(empty)


def eliminate_studies(kb_class, visited):
    """
    Eliminates studies from the kb
    :param kb_class: the class containing the kba nd user kb
    :param visited: list containing the questions that have been asked (to simplify the elimination process)
    :return: List containing all eliminates studies
    """
    size_kb = len(kb_class.kb)
    elim_studies = ''
    i = 0
    # Iterating over all studies in the kb and eliminating those
    # which do not match
    while i < size_kb:
        elim = elimination_update(kb_class.kb[i], kb_class.kb, kb_class.user_kb, visited)
        if elim != 1:
            # Gathering all eliminated studies to save in trace
            elim_studies += ';' + elim['label'] + ' at ' + elim['university']
        # After removal, the items are moved to a lower index in the list.
        if len(kb_class.kb) < size_kb:
            size_kb -= 1
            i -= 1
        i += 1

    if len(elim_studies) == 0:
        elim_studies = 'None'
    else:
        # Cutting off ';'
        elim_studies = elim_studies[1:]

    return elim_studies


def save_trace(question, response, elim_studies):
    """
    Saves the current question, response and elimination studies to a text file (i.e. the trace)
    :param question: current question asked
    :param response: user input to the question
    :param elim_studies: eliminated studies based on user input
    """
    path = './model/trace.txt'
    if os.path.exists(path):
        with open(path, 'a') as file:
            file.write('question: ' + question + "\n")
            if type(response) == list:
                answer = ''
                for item in response:
                    answer += ';' + item
                file.write('response: ' + answer[1:] + "\n")
            else:
                file.write('response: ' + str(response) + "\n")
            file.write('eliminated studies: ' + elim_studies + "\n")
            file.close()
