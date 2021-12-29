import re


def make_user_kb(answer, queries, notes, studies_kb, user_kb, visited):

    # Add diploma for user
    if 'diplomas' not in user_kb.keys() and 'diplomas' not in visited:
        print("1. Creating and Adding Diploma")
        user_kb['diplomas'] = ''    #initalise 'diplomas'
        if re.search('Lise Diploma', answer) or re.search('Label France Education', answer) or re.search('Abitur', answer):
            user_kb['diplomas'] = answer #save answer
            print('diploma saved: ' + user_kb['diplomas'])
            queries.addQuestion("1b. ----> Have you also taken at least 4 AP courses?(yes/no)") #next question - AP courses?
            
        if re.search('AP', answer) or re.search('IB', answer):
            user_kb['diplomas'] = answer #save answer
            print('diploma saved: ' + user_kb['diplomas'])
            queries.addQuestion("----> What subjects did you take?\n choose from chemistry, physics, and mathematics?") #next question - subjects?

        visited.append('diplomas') #mark 'diplomas' as visited
        return
    
    # if diploma not in IB or no AP courses
    if user_kb['diplomas'] != 'IB' and 'AP option' not in user_kb.keys():
        visited.pop(0)  #reset visited
        if answer == 'no':
            notes.addDisclaimer("Check university websites for further info.")
            visited.append('no AP')
        elif answer == 'yes':   
            user_kb['AP option'] = 'yes'    #save answer (user took extra AP courses)
            queries.addQuestion("----> What subjects did you take?\n choose from chemistry, physics, and mathematics?") #next question - AP subjects?
            visited.append('AP option')  #mark as visited
        return

    # Add subjects for user
    if 'subjects' not in user_kb.keys() and 'subjects' not in visited:
        visited.pop(0)  #reset visited
        user_kb['subjects'] = []    #initialise 'subjects'
        print("\n2. Reading Subjects with Regex")
        
    # IB subjects
        if re.search('[Aa]nalytics\&[Aa]pproaches(\sSL|\sHL)?', answer):
            user_kb['subjects'].append('Mathematics HL')

        if re.search('[Mm]athematics(\sSL|\sHL)?', answer):
            match = re.search('[Mm]athematics(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())

    # AP Mathematics
        if re.search('[Cc]alculus(\sA\/B|\sB\/C)?', answer):
            match = re.search('[Cc]alculus(\sA\/B|\sB\/C)?', answer)
            user_kb['subjects'].append(match.group())

    # IB & AP     
        if re.search('[Pp]hysics(\sSL|\sHL|\s1|\s2|\sC)?', answer):
            match = re.search('[Pp]hysics(\sSL|\sHL|\s1|\s2|\sC)?', answer)
            user_kb['subjects'].append(match.group())
        
        if re.search('[Cc]hemistry(\sSL|\sHL)?', answer):
            match = re.search('[Cc]hemistry(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())

        visited.append('subjects')  #mark as visited
        queries.addQuestion("Enter grade for {}".format(user_kb['subjects'][0]))  #next question - grade for 1st subject in user_kb['subjects']
        
        return


    # Add subject grades for user - INITIALISE LOOP
    if 'subjectGrades' not in user_kb.keys() and 'subjectGrades' not in visited and 'subjects' in visited:
        print("\nvisited: " + str(visited))
        visited.pop(0) #reset visited
        print("removing 'subjects' from visited")
        print("\nvisited: " + str(visited))
        visited.append('subjectGrades')    #mark as visited - already here to loop based on 'subjcts' in next if
        print("appending 'subjectGrades' to visited")
        user_kb['subjectGrades'] = []   #initialise - subjectGrades already here to loop in next if
        print("Created subjectGrades")

    if 'subjectGrades' in user_kb.keys() and 'subjectGrades' in visited and 'english level' not in user_kb.keys():
        print("\n3. Saving subject grade\n")
        if len(visited) == 2: # next subject exists
            visited.pop(1)
        if len(user_kb['subjectGrades']) == 1:
            user_kb['subjectGrades'].pop(0)

        # save response
        visited.insert(1, user_kb['subjects'][0])   # add subject to visited
        
        grade = int(answer)
        print("grade: " + str(grade))
        print(user_kb['subjectGrades'])
        if 'AP option' in user_kb.keys() and grade > 5:
            queries.addQuestion("\nThe max grade is 5. Enter grade for {}: ".format(user_kb['subjects'][0]))  
            return
        elif user_kb['diplomas'] == 'IB' and grade > 7:
            queries.addQuestion("\nThe max grade is 7. Enter grade for {}: ".format(user_kb['subjects'][0]))  
            return
            
        user_kb['subjectGrades'].append(grade)  # save grade-answer for user
        user_kb['subjects'].pop(0)  # remove the subject to note as 'completed'

        print("visited: " + str(visited))
        print("user_kb-subjects: " + str(user_kb['subjects']))
        print("user_kb-subjectGrades: " + str(user_kb['subjectGrades']))

        # is this the last subject to check? Then make next question about English tests.
        if len(user_kb['subjects']) == 0: 
            user_kb['english level'] = []  
            if user_kb['diplomas'] in 'IB':
                notes.addDisclaimer("\nYou don't need an English test, since you've studied the IB programme.")
                queries.addQuestion("What would you like to study in uni? Select from the list below.") # move onto preferences
            else:
                queries.addQuestion("\nHave you taken an English test?(y/n)") #next question-move onto English tests
                #visited.clear()
                user_kb['english level'] = [] #initialise
        else:
            queries.addQuestion("\nEnter grade for {}: ".format(user_kb['subjects'][0]))  
        return

        
    # English Level questions
    if 'english level' in user_kb.keys() and 'english level' not in visited and 'english grades' not in user_kb.keys(): 
        print("\nAdding English Question")
        visited.pop(1) #remove 'subject-saved' and 'subjectGrades' from visited
        visited.pop(0) 
        #print("visited: " + str(visited))
        #user_kb['english level'] = [] #initialise
        print("visited: " + str(visited))
        
        if answer == 'no':  # no english test
            queries.addQuestion("Have you followed at least your entire Bachelor’s degree or the last years of your High School from the following countries?\nAustralia, Canada, Ireland, New Zealand, UK and USA.")
            visited.append('abroad')
        elif answer == 'yes':   # directly move onto 'english level' checking
            queries.addQuestion("Which English test did you take? Choose from list below.")
            visited.append('english level')
        return
        
    if 'abroad' in visited:
        if answer == 'no':  # no test and no abroad years, and diploma not IB
            studies_kb.clear()
            visited.clear()
            return
        elif answer == 'yes':  # no test but yes abroad years, study req. may be met
            notes.addDisclaimer("English level may be approved. Check website for further info")
            queries.clearQuestion() # esasında buraya preference ile ilgili sorular gelicek...
            visited.clear()
        return
    
    if 'english level' in visited and 'english grades' not in user_kb.keys():
        # English level for diplomas without subjectGrades but subjects
        print("Checking English test visited: " + str(visited))
        english_level = answer 
        user_kb['english level'] = english_level
        queries.addQuestion("Enter overall score: ") #next question
        user_kb['english grades'] = [] #initialise
        return

    if 'english grades' in user_kb.keys() and 'english grades' not in visited:
        print("Checking English grades before: " + str(visited))
        visited.pop(0) #reset visited - remove 'english level'
        visited.append('english grades') #enter 'english grade' for LOOP
        print("Checking English grades after: " + str(visited))
        queries.addQuestion("Enter {} score: ".format('Reading'))
        queries.addQuestion("Enter {} score: ".format('Listening'))
        queries.addQuestion("Enter {} score: ".format('Speaking '))
        queries.addQuestion("Enter {} score: ".format('Writing'))
        
    # LOOP
    if 'english grades' in visited:
        print("English grades LOOP")
        english_grade = answer
        user_kb['english grades'].append(english_grade) #save grade
        if queries.getQuestionListLen() == 1: #OR if queries.getCurrentQuestion() == "Enter Writing score: ":
            visited.pop()
            visited.append('check english grades')
            print("next question")
        return
        

    '''
        

    if 'english grades' in visited and answer.isnumeric():
        print("english grade visited: " + str(visited)) 
        # makes use of the fact that the grades per section are stored in the same order as they are asked
        for testGrd in user_kb['english grades']:
            if len(testGrd) == 1:
                testGrd.append(float(answer))
                break
        visited.pop(0)
        visited.append('english level')
        print("english grade visited: " + str(visited)) 

        '''
'''
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
'''


'''
    
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
    
        NOTE: with question type: Disclaimer, this part will be added. It does not need a response.
        if answer == 'yes': 
            queries.addQuestion("\nNote that:\nA relevant program is a program with Mathematics (and for some TU/e programs also Physics/Chemistry) at the Dutch pre-university (VWO) level. Your Grade Point Average for the first year must be at least 75%.")
            return
    

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
    
    '''

        
                        
