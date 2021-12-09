import re

def rules_check(answer, queries, study_kb, user_kb):

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

    if (answer in ['TOEFL', 'IELTS', 'CPE', 'CPA', 'TOEIC', 'IB A HL', 'Cambridge B2', 
                'Cambridge C1', 'Cambridge C2', 'IB English programme', 'IB', 'EB']):
        user_kb['english test'] = answer


    english_tests_specific = ['TOEFL', 'IELTS', 'CPE', 'CPA', 'TOEIC'] 

    if ((answer in english_tests_specific or answer in ['IB A HL', 'Cambridge B2', 'Cambridge C1', 'Cambridge C2']) and 
                ((answer + 'overall') not in user_kb.keys())):
        user_kb[answer + 'overall'] = ''
        queries.addQuestion("What is the overall score of the English test?")
    

    if (answer in english_tests_specific and 
                (answer + 'min') not in user_kb.keys()):
        user_kb[answer + 'min'] = ''
        queries.addQuestion("What is the minimum score obtained over all sections?")
        
        


    
            

