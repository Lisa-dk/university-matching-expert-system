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
    # NOTE: the question is printed here, to queries.addQuestion(), this 'if' should be separated into two, see below examples
    if user_kb['diplomas'] == 'Label France Education' and 'english level' not in user_kb.keys():
        print("\nTevfik Fikret High School\nNotre Dame de Sion school and high school\nGalatasaray High School\nSaint Benoît High School\nSaint Joseph High School\nSaint Michel high school\nSainte Pulchérie High School\nSaint Joseph High School\nTevfik Fikret High School\nSchool, middle and high school Küçük Prens")
        approved_school = input("----> Did you graduate from any of the schools above?(yes/no)\n")
        if approved_school == 'no':
            study_kb.clear()
            return

    # Lise Diploma
    # NOTE: the questions are printed here, to queries.addQuestion(), this 'if' should be separated into multiple sections, see below examples
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
        # for IB and the rest
        if re.search('[Aa]nalytics\&[Aa]pproaches(\sSL|\sHL)?', answer):
            user_kb['subjects'].append('Mathematics HL')

        if re.search('[Mm]athematics(\sSL|\sHL)?', answer):
            match = re.search('[Mm]athematics(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())
        
        # AP and the rest
        if re.search('[Cc]alculus(\sA\/B|\sB\/C)?', answer):
            user_kb['subjects'].append('Calculus')
        
        # only AP physics
        if re.search('[Pp]hysics((\s1\&2)|(\sC))', answer):
            user_kb['subjects'].append('Physics')

        # for IB physics
        if re.search('[Pp]hysics((\sSL|\sHL))', answer):
            match = re.search('[Pp]hysics((\sSL|\sHL))', answer)
            user_kb['subjects'].append(match.group())
        
        # for the rest
        #print(answer)
        if re.search('[Pp]hysics', answer):
            user_kb['subjects'].append('Physics')

        # for IB and the rest
        if re.search('[Cc]hemistry(\sSL|\sHL)?', answer):
            match = re.search('[Cc]hemistry(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())

        #print(user_kb['subjects'])
        #print(user_kb['subjects'])

    if 'subjectGrades' not in user_kb.keys() and 'subjects' in user_kb.keys() and user_kb['subjects']!=[]:  
        #print("\n3. Will create subjectGrades if NESTED")
        for study in study_kb:
            if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]):  # True if nested lists, means subjects have grades
                #print("NESTED")
                if 'subjectGrades' not in user_kb.keys():
                    user_kb['subjectGrades'] = []
                    queries.addQuestion("\nEnter grade for {}: ".format(user_kb['subjects'][0]))
                    return
            #print("NOT NESTED")
    
    if 'subjectGrades' in user_kb.keys() and 'english level' not in user_kb.keys() and user_kb['subjects'] != []:
        tempSubj = [user_kb['subjects'][0]]
        grade = answer
        tempSubj.append(grade)
        user_kb['subjectGrades'].insert(0, tempSubj)
        user_kb['subjects'].remove(user_kb['subjects'][0]) 
        if len(user_kb['subjects']) == 0:   # move onto English tests
            queries.addQuestion("\nHave you taken an English test?(y/n)")
            return
        queries.addQuestion("\nEnter grade for {}: ".format(user_kb['subjects'][0]))  
        return

    if 'english level' not in user_kb.keys() and user_kb['diplomas'] not in ['IB', 'EB'] and user_kb['subjectGrades'] != []:
        if answer == 'no':
            study_kb.clear()
        #print("\nAdding English Question")
        user_kb['english level'] = None
        queries.addQuestion("What is your English level?")


    if 'english level' in user_kb.keys():
        for study in study_kb:
            if answer in study['english level']:
                user_kb['english level'] = answer
                
            if user_kb['english level'] is not None and user_kb['english level'] in study.keys() and 'english grades' not in user_kb.keys():
                user_kb['english grades'] = []
                for testGrd in study[user_kb['english level']]:
                    if testGrd[0] != 'overall':
                        queries.addQuestion("\nEnter grade for {}: ".format(testGrd[0]))
                    else:
                        queries.addQuestion("Enter overall score for {}".format(user_kb['english level']))
                    user_kb['english grades'].append([testGrd[0]])
                break

    if 'english grades' in user_kb.keys() and answer.isnumeric():
        # makes use of the fact that the grades per section are stored in the same order as they are asked
        for testGrd in user_kb['english grades']:
            if len(testGrd) == 1:
                testGrd.append(float(answer))
                break


        
                        
