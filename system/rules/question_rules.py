import re


def rules_check(answer, queries, study_kb, user_kb):

    # Adding diplomas
    if 'diplomas' not in user_kb.keys() and 'subjects' not in user_kb.keys():  # first question is about diplomas
        #print("0. Creating and Adding Diploma")
        user_kb['diplomas'] = ''
        if re.search('Lise Diploma', answer):
            user_kb['diplomas'] = 'Lise Diploma'

        if re.search('AP', answer):
            user_kb['diplomas'] = 'AP'

        if re.search('IB', answer):
            user_kb['diplomas'] = 'IB'
        
        if re.search('Label France Education', answer):
            user_kb['diplomas'] = 'Label France Education'

        if re.search('British GCE A Levels', answer):
            user_kb['diplomas'] = 'British GCE A Levels'
    
    # Label France Education has no subject requirements
    if user_kb['diplomas'] == 'Label France Education' and 'english level' not in user_kb.keys():
        print("\nTevfik Fikret High School\nNotre Dame de Sion school and high school\nGalatasaray High School\nSaint Benoît High School\nSaint Joseph High School\nSaint Michel high school\nSainte Pulchérie High School\nSaint Joseph High School\nTevfik Fikret High School\nSchool, middle and high school Küçük Prens")
        approved_school = input("----> Did you graduate from any of the schools above?(yes/no)\n")
        if approved_school == 'no':
            study_kb.clear()
            return

    # Lise Diploma
    if user_kb['diplomas'] == 'Lise Diploma' and 'subjects' not in user_kb.keys():
        AP_extra = input("----> Have you also taken at least 4 AP courses?(yes/no)\n")
        if AP_extra == 'yes':
            user_kb['diplomas'] = 'AP'
            print(user_kb['diplomas'])
        else: 
            print("\nIf you have obtained a regular Lise Diplomasi you must have successfully completed at least your first year at an accredited technical university in a relevant program to meet our admission requirements. List of the accredited technical universities.")
            print("ABDULLAH GÜL ÜNİVERSİTESİ\nACIBADEM MEHMET ALİ AYDINLAR ÜNİVERSİTESİ\nADANA ALPARSLAN TÜRKEŞ BİLİM VE TEKNOLOJİ ÜNİVERSİTESİ\nADIYAMAN ÜNİVERSİTESİ\nAFYON KOCATEPE ÜNİVERSİTESİ")
            approved_school = input("----> Did you graduate from any of the schools above?(yes/no)\n")
            if approved_school == 'no':
                study_kb.clear()
                return
            else: 
                print("\nNote that:\nA relevant program is a program with Mathematics (and for some TU/e programs also Physics/Chemistry) at the Dutch pre-university (VWO) level. Your Grade Point Average for the first year must be at least 75%.\n")
       

    if 'subjects' not in user_kb.keys() and user_kb['diplomas'] != 'Label France Education':
        #print("\n1. Creating user_kb['subjects'] and Adding subject question")
        user_kb['subjects'] = []
        queries.addQuestion("----> What subjects did you take?\n choose from chemistry, physics, and mathematics?")
        return

    # Adding subjects to user facts
    if 'subjects' in user_kb.keys() and 'subjectGrades' not in user_kb.keys():
        #print("\n2. Matching Subjects")
        # only AP physics
        if re.search('[Pp]hysics((\s1\&2)|(\sC))', answer):
            user_kb['subjects'].append('Physics')
        
        # for IB and the rest
        if re.search('[Aa]nalytics\&[Aa]pproaches(\sSL|\sHL)?', answer):
            user_kb['subjects'].append('Mathematics HL')

        # for IB and the rest
        if re.search('[Mm]athematics(\sSL|\sHL)?', answer):
            match = re.search('[Mm]athematics(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())

        # for IB and the rest
        if re.search('[Cc]hemistry(\sSL|\sHL)?', answer):
            match = re.search('[Cc]hemistry(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())
        
        # for IB physics
        if re.search('[Pp]hysics((\sSL|\sHL))', answer):
            match = re.search('[Pp]hysics((\sSL|\sHL))', answer)
            user_kb['subjects'].append(match.group())
        
        # for the rest
        if re.search('[Pp]hysics$', answer):
            user_kb['subjects'].append('Physics')

        # AP and the rest
        if re.search('[Cc]alculus(\sA\/B|\sB\/C)?', answer):
            user_kb['subjects'].append('Calculus')

        #print(user_kb['subjects'])

    if 'subjectGrades' not in user_kb.keys() and 'subjects' in user_kb.keys() and user_kb['subjects']!=[]:  
        #print("\n3. Will create subjectGrades if NESTED")
        for study in study_kb:
            if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]):  # True if nested lists, means subjects have grades
                #print("NESTED")
                if 'subjectGrades' not in user_kb.keys():
                    user_kb['subjectGrades'] = []
            #print("NOT NESTED")
            
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
