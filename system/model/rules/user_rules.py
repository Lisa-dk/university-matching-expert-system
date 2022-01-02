import re

def make_user_kb(answer, queries, notes, studies_kb, user_kb, visited):

    # Do you know what you want to study?
    if 'start' in visited and 'study preference' not in user_kb.keys():

        print("\nSaving Study-preference question:")

        if answer == 'yes': # knows what to study
            queries.addQuestion("--> What are your study preferences?")
            user_kb['study preference'] = [] # initialise study preference
        
        elif answer == 'no': # doesn't know what to study
            queries.addQuestion("---> What is you highschool diploma?")
            visited.remove('start')
            visited.append('study preference') # done with study preference in user_rules
        
        return # no elimination


    # save study preference
    if 'start' in visited and 'study preference' in user_kb.keys(): 
        visited.remove('start')

        print("\nSaving study preference")
        # !!!! NOTE: did not add all descriptions in kb to here
        if re.search('Chemical Engineering', answer):
            user_kb['study preference'].append('Chemical Engineering')
        
        if re.search('Technology', answer):
            user_kb['study preference'].append('Technology')    

        if re.search('Design', answer):
            user_kb['study preference'].append('Design')   

        if re.search('Society', answer):
            user_kb['study preference'].append('Society')  
        
        if re.search('Electrical Engineering', answer):
            user_kb['study preference'].append('Electrical Engineering')

        if re.search('Architecture', answer):
            user_kb['study preference'].append('Architecture')

        if re.search('Automative Engineering', answer):
            user_kb['study preference'].append('Automative Engineering')

        if re.search('Mechanical Engineering', answer):
            user_kb['study preference'].append('Mechanical Engineering')

        if re.search('Innovation', answer):
            user_kb['study preference'].append('Innovation')
        
        if re.search('Industrial Engineering', answer):
            user_kb['study preference'].append('Industrial Engineering')
        
        if re.search('Computer Science', answer):
            user_kb['study preference'].append('Computer Science')
        
        if re.search('Psychology', answer):
            user_kb['study preference'].append('Psychology')

        queries.addQuestion("----> What is your highschool diploma?") # add diploma question
        visited.append('study preference') # done with study-preference in user_rules
        return


    # add IB vs. no-IB diplma
    if 'study preference' in visited and 'diplomas' not in user_kb.keys():

        print("\n1. Creating and Adding Diploma")
        visited.remove('study preference') # reset visited
        user_kb['diplomas'] = '' # initalise 'diplomas'

        # IB diploma
        if re.search('IB', answer):
            user_kb['diplomas'] = answer # save IB
            visited.append('diplomas') # done with diplomas
            print('diploma saved: ' + user_kb['diplomas'])
            queries.addQuestion("----> What subjects did you take?\n choose from chemistry, physics, and mathematics?") #next question - subjects?
        
        # no IB diploma
        elif re.search('Lise Diploma', answer) or re.search('Label France Education', answer) or re.search('Abitur', answer):
            user_kb['diplomas'] = answer # save answer-diploma
            print('no-IB diploma saved: ' + user_kb['diplomas'])
            queries.addQuestion("1b. ----> Have you also taken any AP courses?(yes/no)") #next question - AP courses?
            
        return
    

    # if diploma is not IB
    if 'diplomas' in user_kb.keys() and user_kb['diplomas'] != 'IB' and 'AP courses' not in user_kb.keys(): # 'diplomas' in user.keys() but not IB
        
        print("\nNo-IB") 
        
        if answer == 'no': # no AP courses
            user_kb['AP courses'] = 'no'
            notes.addDisclaimer("Check university websites for further info.")
            visited.append('no AP') # mark as/done with no AP

        elif answer == 'yes':   
            user_kb['AP courses'] = 'yes'    #save answer (user took extra AP courses)
            queries.addQuestion("----> What subjects did you take?\n choose from chemistry, physics, and mathematics?") #next question - AP subjects?
            visited.append('diplomas')  # done with diplomas
        
        return



    # add subjects
    if 'diplomas' in visited and 'subjects' not in user_kb.keys():
        
        print("\nInitialising subjects")
        visited.remove('diplomas')  # reset visited
        user_kb['subjects'] = []    #initialise 'subjects'
        
        print("Reading Subjects with Regex")
        
    # IB subjects
        if re.search('[Aa]nalysis\&[Aa]pproaches(\sSL|\sHL)?', answer):
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
        
        if re.search('[Bb]iology(\sSL|\sHL)?', answer):
            match = re.search('[Bb]iology(\sSL|\sHL)?', answer)
            user_kb['subjects'].append(match.group())

        visited.append('subjects')  # done with subjects
        queries.addQuestion("Enter grade for {}".format(user_kb['subjects'][0]))  #next question - grade for 1st subject in user_kb['subjects']
        
        return


    # add grades of subjects - INITIALISE LOOP
    if 'subjects' in visited and 'subject grades' not in user_kb.keys() and 'subject grades' not in visited:
        
        print("\nCreated subject grades")
        visited.remove('subjects') # reset visited
        visited.append('subject grades')  # mark subject grades as done/visited - already here to loop based on 'subjects' in next if
        user_kb['subject grades'] = []   #initialise - subject grades already here to loop in next if
        

    if 'subject grades' in visited and 'subject grades' in user_kb.keys():
        
        print("\n3. Saving subject's grade")

        if len(visited) == 2: # next subject exists
            visited.pop(1)
        if len(user_kb['subject grades']) == 1:
            user_kb['subject grades'].pop(0)

        visited.insert(1, user_kb['subjects'][0])   # note current subject in loop to visited for elimination as second el in visited[]
        
        # save response-grade
        grade = int(answer)
        
        # invalid grade input above fixed max limit
        if 'AP courses' in user_kb.keys() and grade > 5:
            queries.addQuestion("The max grade is 5. Enter grade for {}: ".format(user_kb['subjects'][0]))  
            return
        elif user_kb['diplomas'] == 'IB' and grade > 7:
            queries.addQuestion("The max grade is 7. Enter grade for {}: ".format(user_kb['subjects'][0]))  
            return
            
        # valid grade input
        user_kb['subject grades'].append(grade)  # save response-grade
        user_kb['subjects'].pop(0)  # remove the current subject from loop/done with the current subject

        print("user_kb-subjects: " + str(user_kb['subjects']))
        print("user_kb-subject grades: " + str(user_kb['subject grades']))

        # is this the last subject to check in user_kb? Then make next question about English tests.
        if len(user_kb['subjects']) == 0: 
            #user_kb['english level'] = []  #hmmmm

            if user_kb['diplomas'] in 'IB': # exception for IB
                notes.addDisclaimer("You don't need an English test, since you've studied the IB programme.")
                queries.addQuestion("Which city do you prefer? Select from the list below.") # move onto general preferences
                print(str(visited))
                visited.pop(1)
                visited.remove('subject grades') # reset visited
                visited.append('check city')
                print(str(visited))

            else: # rest of the diplomas require English tests
                queries.addQuestion("Have you taken an English test?(y/n)") #next question- English test?
                visited.pop(1) # remove subject-saved
                visited.remove('subject grades') # reset visited
                visited.append('english proof')
        else:
            queries.addQuestion("Enter grade for {}: ".format(user_kb['subjects'][0]))  # get next subject in user_kb
        
        return

        
    # determine english level
    if 'english proof' in visited:   # visited only has 'subject grades' and not the subject as well from previous if
        
        print("\nDetermine English Test Question")
        visited.remove('english proof')
        
        # *********** NOTE to self: not finished
        if answer == 'no':  # no english test
            queries.addQuestion("Have you followed at least your entire Bachelor’s degree or the last years of your High School from the following countries?\nAustralia, Canada, Ireland, New Zealand, UK and USA.")
            visited.append('abroad')

        elif answer == 'yes':   # move onto 'english tests' checking
            queries.addQuestion("Which English test did you take? Choose from list below.")
            visited.append('english level') # done with (checking) english level (whether it exists or not)
        
        return # no elimination


    '''    
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
    '''


    # add english test
    if 'english level' in visited and 'english tests' not in user_kb.keys():

        print("\nSaving English Test")
        visited.remove('english level')

        user_kb['english tests'] = ''   # initalise english test
        english_level = answer 
        user_kb['english tests'] = english_level  # save answer
        visited.append('english tests')   # done with english tests - send to elimination

        queries.addQuestion("Enter overall score: ")    # next question
        
        return


    # grades of english test - INITIALISE LOOP
    if 'english tests' in visited and 'english grades' not in user_kb.keys():
        
        print("\nInitialising English Test - Grades")
        visited.remove('english tests')   # reset visited
        # adding English test Questions
        # NOTE: if sections are different from below and not fixed
        # add 'TOEFL sections' for kb and loop over sections in next if to add next Question, Enter {} score.
        queries.addQuestion("Enter {} score: ".format('Reading'))
        queries.addQuestion("Enter {} score: ".format('Listening'))
        queries.addQuestion("Enter {} score: ".format('Speaking '))
        queries.addQuestion("Enter {} score: ".format('Writing'))
        user_kb['english grades'] = [] # initalise before loop
        visited.append('english grades') # mark english test grades as done/visited - already here to loop based on tests sections in next if


    # LOOP
    if 'english grades' in visited: # and next question condition not in user_kb.keys(): ...
        
        print("\nEnglish grades LOOP")
        # save grade answer
        english_grade = answer 
        user_kb['english grades'].append(english_grade) 

        # last question in queries.list
        if queries.getQuestionListLen() == 1: #OR if queries.getCurrentQuestion() == "Enter Writing score: ":
            visited.pop() # empty queries
            visited.append('check english grades')
            queries.addQuestion("---> Which cities do you prefer?")

        return
        
    if ('check english grades' in visited or 'check city' in visited) and 'city' not in user_kb.keys():
        
        print("\nSaving City Preference")
        visited.pop(0)    # reset visited

        # possible regex answers
        user_kb['city'] = []
        if re.search('Eindhoven', answer):
            user_kb['city'].append('Eindhoven')
        
        if re.search('Groningen', answer):
            user_kb['city'].append('Groningen')

        if re.search('Maastricht', answer):
            user_kb['city'].append('Maastricht')
        
        if re.search('Delft', answer):
            user_kb['city'].append('Delft')

        elif re.search('No Preference', answer): # pass on city elimination
            return # no elimination

        visited.append('city')
        return
