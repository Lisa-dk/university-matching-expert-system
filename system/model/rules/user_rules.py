import re

from model.questions import QuestionType
from model.questions import Question


def edit_user_kb(answer, queries, notes, studies_kb, user_kb, visited):
    """
    Processes the user input and provides the next questions through if-then rules.
    :param answer: user input to a question
    :param queries: class of questions
    :param notes: #TODO
    :param studies_kb: kb containing the study programmes
    :param user_kb: kb containing user info
    :param visited: list of passed questions
    :return: Nothing
    """
    # Do you know what you want to study?
    if 'start' in visited and 'study preference' not in user_kb.keys():

        # print("\nSaving Study-preference question:")

        if answer == 'yes':  # knows what to study
            queries.add_question(["What are your study preferences?",
                                  QuestionType.MULTI_SELECT, queries.get_question_options('preferences')])
            user_kb['study preference'] = []  # initialise study preference

        elif answer == 'no':  # doesn't know what to study
            queries.add_question(
                ["What is your high school diploma?",
                 QuestionType.SELECT, queries.get_question_options('diploma')])
            visited.remove('start')
            visited.append('study preference')  # done with study preference in user_rules

        return  # no elimination

    # save study preference
    if 'start' in visited and 'study preference' in user_kb.keys():
        visited.remove('start')

        # print("\nSaving study preference")
        # !!!! NOTE: did not add all descriptions in kb to here
        if type(answer) == list:
            user_kb['study preference'] = answer

       # add diploma
        queries.add_question(["What is your high school diploma?",
                              QuestionType.SELECT, queries.get_question_options('diploma')])  # add diploma question
        visited.append('study preference')  # done with study-preference in user_rules
        return

    # add IB vs. no-IB diploma
    if 'study preference' in visited and 'diplomas' not in user_kb.keys():

        # print("\n1. Creating and Adding Diploma")
        visited.remove('study preference')  # reset visited
        user_kb['diplomas'] = ''  # initialise 'diplomas'

        # IB diploma
        if re.search('IB', answer):
            user_kb['diplomas'] = answer  # save IB
            visited.append('diplomas')  # done with diplomas
            # print('diploma saved: ' + user_kb['diplomas'])
            # next question - subjects?
            queries.add_question([
                                     "Did you take any of the following subjects from IB?",
                                     QuestionType.MULTI_SELECT,
                                     queries.get_question_options('subjects IB')])  # next question - subjects?

        # no IB diploma
        elif re.search('Lise Diploma', answer) or re.search('Label France Education', answer) or re.search('Abitur',
                                                                                                           answer):
            user_kb['diplomas'] = answer  # save answer-diploma
            # print('no-IB diploma saved: ' + user_kb['diplomas'])
            # next question - AP courses?
            queries.add_question(["Have you also taken any AP courses?", QuestionType.SELECT,
                                  queries.get_question_options('yes-no question')])  # next question - AP courses?

        return

    # if diploma is not IB
    if 'diplomas' in user_kb.keys() and user_kb['diplomas'] != 'IB' and 'AP courses' not in user_kb.keys():  # 'diplomas' in user.keys() but not IB

        # print("\nNo-IB")

        if answer == 'no':  # no AP courses
            user_kb['AP courses'] = 'no'
            notes.addDisclaimer(
                "As you did not take additional AP courses, we suggest you check university websites for further information for application with a {} diploma. ".format(user_kb['diplomas']))
            visited.append('None')  # mark as/done with no AP

        elif answer == 'yes':
            user_kb['AP courses'] = 'yes'  # save answer (user took extra AP courses)
            queries.add_question([
                                     "Did you take any of the following subjects from AP?",
                                     QuestionType.MULTI_SELECT,
                                     queries.get_question_options('subjects AP')])  # next question - AP subjects?
            visited.append('diplomas')  # done with diplomas

        return

    # add subjects
    if 'diplomas' in visited and 'subjects' not in user_kb.keys():

        # print("\nInitialising subjects")
        visited.remove('diplomas')  # reset visited
        if type(answer) == list:
            user_kb['subjects'] = answer

            if 'None of the above' in answer:
                notes.addDisclaimer(
                    "You have not met the subject requirements of any study programme in the field of engineering for a Dutch university. ")
                visited.append('None')  # mark as/done with no AP
                return

        visited.append('subjects')  # done with subjects
        print(user_kb['subjects'][0])
        # queries.add_question("Enter grade for {}:".format(user_kb['subjects'][0]))  # next question - grade for 1st subject in user_kb['subjects']
        queries.add_question(["Enter grade for {}:".format(user_kb['subjects'][0]), QuestionType.TEXT_FIELD,
                              None])  # next question - grade for 1st subject in user_kb['subjects']

        return

    # add grades of subjects - INITIALISE LOOP
    if 'subjects' in visited and 'subject grades' not in user_kb.keys() and 'subject grades' not in visited:
        # print("\nCreated subject grades")
        visited.remove('subjects')  # reset visited
        visited.append(
            'subject grades')  # mark subject grades as done/visited - already here to loop based on 'subjects' in next if
        user_kb['subject grades'] = []  # initialise - subject grades already here to loop in next if

    if 'subject grades' in visited and 'subject grades' in user_kb.keys():

        # print("\n3. Saving subject's grade")

        if len(visited) == 2:  # next subject exists
            visited.pop(1)
        if len(user_kb['subject grades']) == 1:
            user_kb['subject grades'].pop(0)

        visited.insert(1, user_kb['subjects'][
            0])  # note current subject in loop to visited for elimination as second el in visited[]

        # save response-grade
        grade = int(answer)

        # invalid grade input above fixed max limit
        if 'AP courses' in user_kb.keys() and grade > 5:
            # queries.add_question("The max grade is 5 for AP courses. Enter grade for {}: ".format(user_kb['subjects'][0]))
            queries.add_question(
                ["The max grade is 5 for AP courses.\nEnter grade for {}: ".format(user_kb['subjects'][0]),
                 QuestionType.TEXT_FIELD, None])
            return
        elif user_kb['diplomas'] == 'IB' and grade > 7:
            # queries.add_question("The max grade is 7 for IB subjects. Enter grade for {}: ".format(user_kb['subjects'][0]))
            queries.add_question(
                ["The max grade is 7 for IB subjects.\nEnter grade for {}: ".format(user_kb['subjects'][0]),
                 QuestionType.TEXT_FIELD, None])
            return

        # valid grade input
        user_kb['subject grades'].append(grade)  # save response-grade
        user_kb['subjects'].pop(0)  # remove the current subject from loop/done with the current subject

        # print("user_kb-subjects: " + str(user_kb['subjects']))
        # print("user_kb-subject grades: " + str(user_kb['subject grades']))

        # is this the last subject to check in user_kb? Then make next question about English tests.
        if len(user_kb['subjects']) == 0:
            # user_kb['english level'] = []  #hmmmm

            if user_kb['diplomas'] in 'IB':  # exception for IB
                #notes.addDisclaimer(
                #    "You don't need an English test, since you've studied the IB programme according to the English-level requirements of the study programs in our system.")
                # queries.add_question("Which cities do you prefer? You may select multiple cities. (Eindhoven, Groningen, Maastricht, Delft, Enschede, I don't mind)")  # move onto general preferences
                queries.add_question([
                                         "Which cities do you prefer? You may select multiple cities.",
                                         QuestionType.MULTI_SELECT,
                                         queries.get_question_options('cities')])  # move onto general preferences
                # print(str(visited))
                visited.pop(1)
                visited.remove('subject grades')  # reset visited
                visited.append('check city')
                # print(str(visited))

            else:  # rest of the diplomas require English tests
                queries.add_question(["Have you taken an English test?", 
                                      QuestionType.SELECT,
                                      queries.get_question_options('yes-no question')])  # next question- English test?
                visited.pop(1)  # remove subject-saved
                visited.remove('subject grades')  # reset visited
                visited.append('english proof')
        else:
            # queries.add_question("Enter grade for {}: ".format(user_kb['subjects'][0]))  # get next subject in user_kb
            queries.add_question(["Enter grade for {}: ".format(user_kb['subjects'][0]), QuestionType.TEXT_FIELD,
                                  None])  # get next subject in user_kb

        return

    # determine english level
    if 'english proof' in visited:  # visited only has 'subject grades' and not the subject as well from previous if

        # print("\nDetermine English Test Question")
        visited.remove('english proof')

        # *********** NOTE to self: not finished
        if answer == 'no':  # no english test
            notes.addDisclaimer(
                                    "You need an English Test with a {} diploma. ".format(user_kb['diplomas']))
            visited.append('None')  # mark as/done with no AP

        elif answer == 'yes':  # move onto 'english tests' checking
            # queries.add_question("Which English test did you take? (TOEFL iBT, IELTS (academic), CPE, CAE)")
            queries.add_question(
                ["Which English test did you take?", 
                 QuestionType.SELECT,
                 queries.get_question_options('English test')])
            visited.append('english level')  # done with (checking) english level (whether it exists or not)

        return  # no elimination

    '''
    # add english test
    if 'english level' in visited and 'english tests' not in user_kb.keys():
        print("\nSaving English Test")
        visited.remove('english level')

        user_kb['english tests'] = ''  # initialise english test
        english_level = answer
        user_kb['english tests'] = english_level  # save answer
        visited.append('english tests')  # done with english tests - send to elimination

        user_kb['english sections'] = ['Overall', 'Reading', 'Listening', 'Speaking', 'Writing'] # build list
        print(user_kb['english sections'][0])
        queries.add_question(["Enter {} score: ".format(user_kb['english sections'][0]), QuestionType.TEXT_FIELD, None])  # next question
        user_kb['english grades'] = []  # initialise 

        if re.search('[Nn]one of the above', answer):
            notes.addDisclaimer(
                "You need to have taken an appropriate english test (e.g. TOEFL iBT) as the english level from your diploma is insufficient. ")
            visited.append('None')  # mark as/done with no AP

        return
    '''
    
    # grades of english test - INITIALISE LOOP
    if 'english tests' in visited and 'english grades' not in user_kb.keys():
        # print("\nInitialising English Test - Grades")
        visited.remove('english tests')  # reset visited
        # adding English test Questions
        # NOTE: if sections are different from below and not fixed
        # add 'TOEFL sections' for kb and loop over sections in next if to add next Question, Enter {} score.
        # queries.add_question("Enter {} score: ".format('Reading'))
        queries.add_question(["Enter {} score: ".format('Reading'), QuestionType.TEXT_FIELD, None])
        # queries.add_question("Enter {} score: ".format('Listening'))
        queries.add_question(["Enter {} score: ".format('Listening'), QuestionType.TEXT_FIELD, None])
        # queries.add_question("Enter {} score: ".format('Speaking '))
        queries.add_question(["Enter {} score: ".format('Speaking '), QuestionType.TEXT_FIELD, None])
        # queries.add_question("Enter {} score: ".format('Writing'))
        queries.add_question(["Enter {} score: ".format('Writing'), QuestionType.TEXT_FIELD, None])
        user_kb['english grades'] = []  # initialise before loop
        visited.append(
            'english grades')  # mark english test grades as done/visited - already here to loop based on tests sections in next if
    
    '''

    # grades of english test - INITIALISE LOOP
    if 'english tests' in visited:
        print("\nInitialising English Test - Grades")
        print(queries)

        # if grade of section above max grade, add different question
        test = user_kb['english tests']
        for section in Question.english_test_max_grade(test):
            print("in loop")
            if section[0] == user_kb['english sections'][0] and answer > float(section[0][1]): # if section in test matches user section checked but grade is higher than max grade of section
                print("wrong grade")
                queries.add_question(
                    ["The maximum grade for the {} grade is {}.\nEnter {} score: ".format(user_kb['english sections'][0], section[0][1], user_kb['english sections'][0]),
                    QuestionType.TEXT_FIELD, None])  # next question
                return
            elif section[0] == user_kb['english sections'][0] and answer <= float(section[0][1]):
                print("valid grade")
                user_kb['english sections'].pop(0)  # next section
                queries.add_question(["Enter {} score: ".format(user_kb['english sections'][0]), QuestionType.TEXT_FIELD, None])
                break
        
        visited.remove('english tests')  # reset visited
        english_grade = answer
        user_kb['english grades'].append(english_grade)

        # last question in queries.list
        if  user_kb['english sections'] == 0:  # OR if queries.getCurrentQuestion() == "Enter Writing score: ":
            print("adding cities question")
            #visited.pop()  # empty queries
            #visited.append('check english grades')
            queries.add_question([
                                     "Which cities do you prefer? You may select multiple cities.",
                                     QuestionType.MULTI_SELECT, queries.get_question_options('cities 2')])
        # visited appended check 
        visited.append(
            'check english grades')  # mark english test grades as done/visited - already here to loop based on tests sections in next if

        return

    '''
    # LOOP
    if 'english grades' in visited:  # and next question condition not in user_kb.keys(): ...

        # print("\nEnglish grades LOOP")
        # save grade answer
        english_grade = answer
        user_kb['english grades'].append(english_grade)

        # last question in queries.list
        if queries.get_questionlist_len() == 1:  # OR if queries.getCurrentQuestion() == "Enter Writing score: ":
            #visited.pop()  # empty queries
            #visited.append('check english grades')
            queries.add_question([
                                     "Which cities do you prefer? You may select multiple cities.",
                                     QuestionType.MULTI_SELECT, queries.get_question_options('cities 2')])
        return
    

    # Checking City 
    if ('check english grades' in visited or 'check city' in visited) and 'city' not in user_kb.keys():

        # print("\nSaving City Preference")
        visited.pop(0)  # reset visited

        if "I don't mind" in answer:  # pass on city elimination
            visited.append("pass city")
            # no elimination, do nothing
        else:
            # else, possible regex answers
            if type(answer) == list:
                user_kb['city'] = answer
                visited.append('city')

        queries.add_question(["Do you prefer a multidisciplinary study?", QuestionType.SELECT,
                              queries.get_question_options('yes-no_preference question')])
        return

    # Multidisciplinary 
    if ('city' in visited or 'pass city' in visited) and 'multidisciplinary' not in user_kb.keys():

        # print("\nSaving Multidisciplinary Preference")
        visited.pop(0)  # reset visited

        if answer == 'yes':  # those that are not will be eliminated
            visited.append('multidisciplinary')
        elif answer == "I don't mind":  # pass
            visited.append('pass multidisciplinary')
            # no elimination, do nothing

        queries.add_question(["Would you like to take an entrance test?", QuestionType.SELECT,
                              queries.get_question_options('yes-no_preference question')])
        return

    # Entrance Exam
    if (
            'multidisciplinary' in visited or 'pass multidisciplinary' in visited) and 'entrance exam' not in user_kb.keys():

        # print("\nSaving Entrance Exam Preference")
        visited.pop(0)  # reset visited

        if answer == 'no':  # no, the user doesn't want the studies with entrance exam, those that have will be eliminated
            visited.append('entrance exam')
        elif answer == "I don't mind":  # pass
            visited.append('pass entrance exam')
            # no elimination, do nothing

        queries.add_question([
                                 "Would you like to take a study choice check? Note that, sometimes this is part of the selection procedure.",
                                 QuestionType.SELECT, queries.get_question_options('yes-no_preference question')])
        return

    # Study Choice Check
    if ('entrance exam' in visited or 'pass entrance exam' in visited) and 'study choice check' not in user_kb.keys():

        # print("\nSaving Study Choice Check Preference")
        visited.pop(0)  # reset visited

        if answer == 'yes':  # studies not offering study choice check will be eliminated
            visited.append('study choice check')
        elif answer == "I don't mind":  # pass
            visited.append('pass study choice check')
            # no elimination, do nothing

        queries.add_question(["Would you like to do research in university?", QuestionType.SELECT,
                              queries.get_question_options('yes-no_preference question')])
        return

    # Research
    if ('study choice check' in visited or 'pass study choice check' in visited) and 'research' not in user_kb.keys():

        # print("\nSaving Research Preference")
        visited.pop(0)  # reset visited

        if answer == 'yes':  # studies not offering research will be eliminated
            visited.append('research')
        elif answer == "I don't mind":  # pass
            visited.append('pass research')
            # no elimination, do nothing

        queries.add_question([
                                 "Do you prefer a study with practical/tutorial oriented approach, perhaps with hands-on/lab experience?",
                                 QuestionType.SELECT, queries.get_question_options('yes-no_preference question')])
        return

    # Practical-oriented
    if ('research' in visited or 'pass research' in visited) and 'practical oriented' not in user_kb.keys():

        # print("\nSaving Practical-Oriented Preference")
        visited.pop(0)  # reset visited

        if answer == 'yes':  # studies not offering practical-oriented approach will be eliminated
            visited.append('practical oriented')
        elif answer == "I don't mind":  # pass
            visited.append('pass practical oriented')
            # no elimination, do nothing

        queries.add_question(["Do you prefer a study with project approach?", QuestionType.SELECT,
                              queries.get_question_options('yes-no_preference question')])
        return

    # Project-oriented
    if (
            'practical oriented' in visited or 'pass practical oriented' in visited) and 'project oriented' not in user_kb.keys():

        # print("\nSaving Project-Oriented Preference")
        visited.pop(0)  # reset visited

        if answer == 'yes':  # studies not offering project oriented approach will be eliminated
            visited.append('project oriented')
        elif answer == "I don't mind":  # pass
            visited.append('pass project oriented')
            # no elimination, do nothing

        queries.add_question([
                                 "Do you mind applying to a numerus fixus study? Note that, numerus fixus study programs have a limited capacity and therefore, may have further requirements such as entrance exam, or portfolio.",
                                 QuestionType.SELECT, queries.get_question_options('yes-no_preference question')])
        return

    # Numerus Fixus
    if ('project oriented' in visited or 'pass project oriented' in visited) and 'numerus fixus' not in user_kb.keys():

        # print("\nSaving Numerus Fixus Preference")
        visited.pop(0)  # reset visited

        if answer == 'no':  # studies that are numerus fixus will be eliminated
            visited.append('project oriented')
        elif answer == "I don't mind":  # pass
            visited.append('pass project oriented')
            # no elimination, do nothing

        #notes.addDisclaimer("You have reached the end of questionnaire.")
        return
