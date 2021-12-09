from questions import QuestionType

def rules_check(question, study_kb, user_kb):

    if question == QuestionType.SUBJECT:
        for subject in study_kb['subjects']:
            if subject not in user_kb[question]:
                return False
    return True

    
    if user_kb['english level'] in study_kb['english level']:
        return True
    
            

