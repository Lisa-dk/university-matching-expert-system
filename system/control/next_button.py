from model.rules.question_rules import rules_check
from model.rules.elimination_rules import elimination_update


# Updates the question list by iterating over all rules and updating the question textfield.
def load_new_question(question_field, kb_class, question_class, question, input_field):
    # obtaining the input
    # qInput = input_field.input_text.get("1.0", "end-1c")
    q_input = input_field.get_chosen_option()
    if q_input == "":
        # TODO: add pop-up asking for question input
        # Stay with current question
        pass
    else:
        # checking over the rules and removing the question
        rules_check(q_input, question_class, kb_class.kb, kb_class.user_kb)
        question_class.remove_question(question)
        eliminate_studies(kb_class)
        # noting whether there are questions left.
        empty = 0 if len(question_class.get_questions()) > 0 else 1
        question_field.update(empty)


# Eliminate studies from the kb
def eliminate_studies(kb_class):
    size_kb = len(kb_class.kb)
    i = 0
    # Iterating over all studies in the kb and eliminating those
    # which do not match
    while i < size_kb:
        elimination_update(kb_class.kb[i], kb_class.kb, kb_class.user_kb)
        # After removal, the items are moved to a lower index in the list.
        if len(kb_class.kb) < size_kb:
            size_kb -= 1
            i -= 1
        i += 1
