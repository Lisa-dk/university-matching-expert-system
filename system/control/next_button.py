from model.rules.question_rules import rules_check
from model.rules.elimination_rules import elimination_update

def loadNewQuestion(questionField, kbClass, questionClass, question, inputField):
    input = inputField.inputText.get("1.0", "end-1c")
    rules_check(input, questionClass, kbClass.kb, kbClass.user_kb)
    questionClass.removeQuestion(question)
    eliminate_studies(kbClass)
    EMPTY = 0 if len(questionClass.getQuestions()) > 0 else 1    
    questionField.update(EMPTY)

    
def eliminate_studies(kbClass):
        size_kb = len(kbClass.kb)
        i = 0
        # Iterating over all studies in the kb and eliminating those
        # which do not match
        while i < size_kb:
            elimination_update(kbClass.kb[i], kbClass.kb, kbClass.user_kb)
            # After removal, the items are moved to a lower index in the list.
            if len(kbClass.kb) < size_kb:
                size_kb -= 1
                i -= 1
            i += 1
