from model.rules.question_rules import rules_check
from model.rules.elimination_rules import elimination_update
from model.rules.user_rules import edit_user_kb
from tkinter import messagebox


# Updates the question list by iterating over all rules and updating the question textfield.
def load_new_question(question_field, kb_class, question_class, question, input_field):
    # edit_user_kb(answer, queries, notes, studies_kb, user_kb, visited):
    # obtaining the input
    # qInput = input_field.input_text.get("1.0", "end-1c")
    answer = input_field.get_chosen_option()
    print(answer)
    if answer == "":
        # Stay with current question
        messagebox.showwarning("Warning", "Please select an option to continue")
    else:
        # checking over the rules and removing the question
        edit_user_kb(answer, question_class, question_field.disclaimer, kb_class.kb, kb_class.user_kb, question_field.visited)
        question_class.remove_question(question)
        eliminate_studies(kb_class, question_field.visited)
        # eliminate_studies(kb_class)
        # noting whether there are questions left.
        empty = 0 if len(question_class.get_questions()) > 0 else 1
        question_field.update(empty)


# Eliminate studies from the kb
def eliminate_studies(kb_class, visited):
    size_kb = len(kb_class.kb)
    i = 0
    # Iterating over all studies in the kb and eliminating those
    # which do not match
    while i < size_kb:
        elimination_update(kb_class.kb[i], kb_class.kb, kb_class.user_kb, visited)
        # After removal, the items are moved to a lower index in the list.
        if len(kb_class.kb) < size_kb:
            size_kb -= 1
            i -= 1
        i += 1
