import re

def rules_check(answer, queries, study_kb, user_kb):

    # Adding subjects to user facts
    if 'subjects' not in user_kb.keys():
        user_kb['subjects'] = []
        if re.search('chemistry', answer):
            user_kb['subjects'].append('chemistry')

        if re.search('mathematics', answer):
            user_kb['subjects'].append('mathematics')

        if re.search('physics', answer):
            user_kb['subjects'].append('physics')
    

    if 'english test' not in user_kb.keys():
        user_kb['english test'] = None
        queries.addQuestion("What English test did you take?")

    # case for general english test
    if (answer in ['TOEFL', 'IELTS', 'CPE', 'CPA', 'TOEIC', 'IB A HL', 'Cambridge B2', 
                'Cambridge C1', 'Cambridge C2', 'IB English programme', 'IB', 'EB']):
        user_kb['english test'] = answer


    english_tests_specific = ['TOEFL', 'IELTS', 'CPE', 'CPA', 'TOEIC'] 

    # If a minimum overall score is required, for any university, ask the overall score and add the field 
    if ((answer in english_tests_specific or answer in ['IB A HL', 'Cambridge B2', 'Cambridge C1', 'Cambridge C2']) and 
                ((answer + 'overall') not in user_kb.keys())):
        user_kb[answer + 'overall'] = ''
        queries.addQuestion("What is the overall score of the English test?")
    

    # if a minimum per section is required for an English test for any uni, ask the question and add the field
    if (answer in english_tests_specific and 
                (answer + 'min') not in user_kb.keys()):
        user_kb[answer + 'min'] = ''
        queries.addQuestion("What is the minimum score obtained over all sections?")
        
        


    
            

