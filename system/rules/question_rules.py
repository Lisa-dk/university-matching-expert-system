import re


def rules_check(answer, queries, study_kb, user_kb):

    # Adding diplomas
    if 'diplomas' not in user_kb.keys():  # first question is about diplomas
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
    if re.search('Chemistry', answer):
        user_kb['subjects'].append('Chemistry')

    if re.search('Mathematics', answer):
        user_kb['subjects'].append('Mathematics')
    '''
    # an addition-IB
    if re.search('MathematicsHL', answer):
        user_kb['subjects'].append('MathematicsHL')
    
    # another addition-IB
    if re.search('PhysicsHL', answer):
        user_kb['subjects'].append('PhysicsHL')
    '''
    # an addition-AP
    if re.search('CalculusA/B', answer):
        user_kb['subjects'].append('CalculusA/B')
    
    # another addition-AP
    if re.search('CalculusB/C', answer):
        user_kb['subjects'].append('CalculusB/C')
    
    '''
    # another addition-AP
    if re.search('Physics1&2', answer):
        user_kb['subjects'].append('Physics1&2')
    
    # another addition-AP
    if re.search('Physics1&2', answer):
        user_kb['subjects'].append('PhysicsC')
    '''

    if re.search('Physics', answer):
        user_kb['subjects'].append('Physics')

    if 'subjectGrades' not in user_kb.keys():  
        for study in study_kb:
            if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]):  # True if nested lists, means subjects have grades
                if 'subjectGrades' not in user_kb.keys():
                    user_kb['subjectGrades'] = []
            
    if 'subjectGrades' in user_kb.keys() and 'english level' not in user_kb.keys():    
        for subject in user_kb['subjects']:
            tempSubj = [subject]
            grade = input("Enter grade for {}: ".format(subject))
            tempSubj.append(grade)
            user_kb['subjectGrades'].append(tempSubj)

    if 'english level' not in user_kb.keys() and user_kb['diplomas'] not in ['IB', 'EB']:
        user_kb['english level'] = None
        queries.addQuestion("What is your English level?")

    # case for general english level
    if 'english level' in user_kb.keys():
        for study in study_kb:
            if answer in study['english level']:
                user_kb['english level'] = answer
            
            if (user_kb['english level'] is not None and
                    (user_kb['english level'] + ' overall') in study.keys() and answer == user_kb['english level'] and
                    (answer + ' overall') not in user_kb.keys()):
                user_kb[answer + ' overall'] = ''
                queries.addQuestion("What is the overall score of the english level?")
                break

    # if a minimum per section is required for an english level for any uni, ask the question and add the field
    if answer in ['TOEFL', 'IELTS', 'CPE', 'CAE', 'TOEIC'] and (answer + 'min') not in user_kb.keys():
        user_kb[answer + 'min'] = ''
        queries.addQuestion("What is the minimum score obtained over all sections?")
