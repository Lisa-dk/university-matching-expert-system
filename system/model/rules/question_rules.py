import re


def rules_check(answer, queries, study_kb, user_kb):

    # Add diploma for student
    if 'diplomas' not in user_kb.keys() and 'subjects' not in user_kb.keys():  # first question is about diplomas
        #print("0. Creating and Adding Diploma")
        user_kb['diplomas'] = ''
        if re.search('Lise Diploma', answer):
            user_kb['diplomas'] = 'Lise Diploma'
            queries.addQuestion("----> Have you also taken at least 4 AP courses?(yes/no)") # adding next question to queries
            return 
            
        if re.search('AP', answer):
            user_kb['diplomas'] = 'AP'

        if re.search('IB', answer):
            user_kb['diplomas'] = 'IB'
        
        if re.search('Label France Education', answer):
            user_kb['diplomas'] = 'Label France Education'
            queries.addQuestion("\nTevfik Fikret High School\nNotre Dame de Sion school and high school\nGalatasaray High School\nSaint Benoît High School\nSaint Joseph High School\nSaint Michel high school\nSainte Pulchérie High School\nSaint Joseph High School\nTevfik Fikret High School\nSchool, middle and high school Küçük Prens\n----> Did you graduate from any of the schools above?(yes/no)")
            return

        if re.search('British GCE A Levels', answer):
            user_kb['diplomas'] = 'British GCE A Levels'
    
    # Label France Education - diploma has no subject requirements
    if user_kb['diplomas'] == 'Label France Education' and 'english level' not in user_kb.keys() and 'subjects' not in user_kb.keys():
        # checking whether the student graduated from the French list of schools mentioned previous
        if answer == 'no':
            study_kb.clear()
            return
        else:
            queries.addQuestion("\nHave you taken an English test?(y/n)")
            user_kb['subjects'] = []    # needed for 'english level' if condition to be recognized
            return

    # Lise Diploma
    if user_kb['diplomas'] == 'Lise Diploma' and 'subjects' not in user_kb.keys():        
        # check answer for extra AP (y/n)
        if answer == 'yes':
            # change diploma to AP
            user_kb['diplomas'] = 'AP'
        else:
            # if no addiional AP subjects, ask whether the student completed their first year at uni listed
            user_kb['diplomas'] = 'Regular Lise Diploma' # change diploma for student
            queries.addQuestion("If you have obtained a regular Lise Diplomasi you must have successfully completed at least your first year at an accredited technical university in a relevant program to meet our admission requirements. List of the accredited technical universities.\nABDULLAH GÜL ÜNİVERSİTESİ\nACIBADEM MEHMET ALİ AYDINLAR ÜNİVERSİTESİ\nADANA ALPARSLAN TÜRKEŞ BİLİM VE TEKNOLOJİ ÜNİVERSİTESİ\nADIYAMAN ÜNİVERSİTESİ\nAFYON KOCATEPE ÜNİVERSİTESİ\n\n----> Did you graduate from any of the schools above?(yes/no)")
            return

    # Regular Lise Diploma - check answer for first year at listed uni (y/n)
    if user_kb['diplomas'] == 'Regular Lise Diploma' and 'subjects' not in user_kb.keys():
        #print("Checking answer for Regular Lise Diploma")
        if  answer == 'no':
            study_kb.clear()
            return
        '''
        NOTE: with question type: Disclaimer, this part will be added. It does not need a response.
        if answer == 'yes': 
            queries.addQuestion("\nNote that:\nA relevant program is a program with Mathematics (and for some TU/e programs also Physics/Chemistry) at the Dutch pre-university (VWO) level. Your Grade Point Average for the first year must be at least 75%.")
            return
        '''

    # Create subjects list for student
    if 'subjects' not in user_kb.keys() and user_kb['diplomas'] != 'Label France Education':
        #print("\n1. Creating user_kb['subjects'] and Adding subject question")
        user_kb['subjects'] = []
        queries.addQuestion("----> What subjects did you take?\n choose from chemistry, physics, and mathematics?")
        return

    # Add subjects for student
    if 'subjects' in user_kb.keys() and 'subjectGrades' not in user_kb.keys() and user_kb['diplomas'] != 'Label France Education':
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
        if re.search('[Pp]hysics$', answer):
            user_kb['subjects'].append('Physics')

        # for IB and the rest
        if re.search('[Cc]hemistry(\sSL|\sHL)?', answer):
            match = re.search('[Cc]hemistry(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())

    # Checking whether subjects have grades in the kb
    if 'subjectGrades' not in user_kb.keys() and 'subjects' in user_kb.keys() and user_kb['subjects']!=[]:  
        #print("\n3. Will create subjectGrades if NESTED")
        for study in study_kb:
            # create subjectGrades list in student's dict if subjects have grades in study
            if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]):  # True if nested lists, means subjects have grades
                #print("NESTED")
                if 'subjectGrades' not in user_kb.keys():
                    user_kb['subjectGrades'] = []
                    queries.addQuestion("\nEnter grade for {}: ".format(user_kb['subjects'][0]))
                    return
            # move onto English questions, if no grades for subjects in study 
            #print("NOT NESTED")
            # if IB, ask IB subject and grade
            if user_kb['diplomas']=='IB':
                queries.addQuestion("\nWas your IB was entirely conducted in the English language? If not, enter 'yes' if you have taken English A HL. (y/n)")
                user_kb['subjects'] = [] # needed for 'english level' if condition to be recognized
                return
    
    # Save subjects and grades together as a list, in new list 'subjectGrades' for student
    if 'subjectGrades' in user_kb.keys() and 'english level' not in user_kb.keys() and user_kb['subjects'] != []:
        #print("\n3. Reading subject grades\n")
        tempSubj = [user_kb['subjects'][0]]
        grade = answer
        tempSubj.append(grade)
        user_kb['subjectGrades'].insert(0, tempSubj)
        user_kb['subjects'].remove(user_kb['subjects'][0]) 
        if len(user_kb['subjects']) == 0:   # since now subjects have grades, no need or subjects list only
            queries.addQuestion("\nHave you taken an English test?(y/n)") # move onto English tests
            return
        queries.addQuestion("\nEnter grade for {}: ".format(user_kb['subjects'][0]))  
        return

    # English Level Questions for diplomas with subjectGrades
    if 'english level' not in user_kb.keys(): #and user_kb['diplomas'] not in ['IB', 'EB']:
        #print("\nAdding English Question")
        user_kb['english level'] = None
        if answer == 'no':
            queries.addQuestion("Have you followed at least your entire Bachelor’s degree or the last 3 years of your High School from the following countries?\nOR Is you nationality from the following countries?\nAustralia, Canada, Ireland, New Zealand, UK and USA.")
            return
        if answer == 'yes':
            queries.addQuestion("What is your English level?")
            return
        

    if 'english level' in user_kb.keys() and user_kb['english level'] == None:
        # checking if other requirements (native, abroad etc.) are satisfied if no englist test
        if answer == 'no':
            study_kb.clear()
            return
        if answer == 'yes':
            return
        else:
            # English level for diplomas without subjectGrades but subjects
            #print("Cheking if English test entered is valid")
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


        
                        
