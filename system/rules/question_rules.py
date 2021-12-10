import re

def rules_check(answer, queries, study_kb, user_kb):

    # Adding diplomas
    if 'diplomas' not in user_kb.keys(): # first question is about diplomas
        user_kb['diplomas'] = ''
        if re.search('Regular Lise Diploma', answer):
            user_kb['diplomas'] = 'Regular Lise Diploma'

        if re.search('AP', answer):
            user_kb['diplomas'] = 'AP'

        if re.search('IB', answer):
            user_kb['diplomas'] = 'IB'
        
        if re.search('Label France Education', answer):
            user_kb['diplomas'] = 'Label France Education'

        if re.search('British GCE A Levels', answer):
            user_kb['diplomas'] = 'British GCE A Levels'
        
            
    if 'subjects' not in user_kb.keys():
        user_kb['subjects'] = []
        queries.addQuestion("What subjects did you take?\n choose from chemistry, physics, and mathematics?")

    # Adding subjects to user facts
    if re.search('chemistry', answer):
        user_kb['subjects'].append('chemistry')

    if re.search('mathematics', answer):
        user_kb['subjects'].append('mathematics')

    if re.search('physics', answer):
        user_kb['subjects'].append('physics')
    

    if 'english level' not in user_kb.keys() and user_kb['diplomas'] not in ['IB', 'EB']:
        user_kb['english level'] = None
        queries.addQuestion("What is your English level?")

    # case for general english level
    if 'english level' in user_kb.keys():
        for study in study_kb:
            if answer in study['english level']:
                user_kb['english level'] = answer
            
            if (user_kb['english level'] != None and 
                    (user_kb['english level'] + ' overall') in study.keys() and answer == user_kb['english level'] and
                    (answer + ' overall') not in user_kb.keys()):
                user_kb[answer + ' overall'] = ''
                queries.addQuestion("What is the overall score of the english level?")
                break

    # if a minimum per section is required for an english level for any uni, ask the question and add the field
    if (answer in ['TOEFL', 'IELTS', 'CPE', 'CAE', 'TOEIC']  and 
                (answer + 'min') not in user_kb.keys()):
        user_kb[answer + 'min'] = ''
        queries.addQuestion("What is the minimum score obtained over all sections?")
        
        


    
            

