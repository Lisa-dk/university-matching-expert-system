def elimination_update(study, studies_kb, user_kb, visited):

    # matching diplomas
    if 'diplomas' in visited:
        print("\n1. Eliminate diplomas")
        if user_kb['diplomas'] not in study['diplomas']:
            studies_kb.remove(study)
            print("removed: " + study['label'])
            return
    
    if 'no AP' in visited:
        print("\n1b. Eliminate all studies")
        studies_kb.remove(study)
        return
    
    '''
    if 'AP option' in visited:
        print("\n1. Eliminate AP")
        print(user_kb['AP option'])
        print(study['AP option'])
        if user_kb['AP option'] != study['AP option']:
            studies_kb.remove(study)
            print("removed: " + study['label'])
            return
    '''
    
    if 'subjects' in visited :
        print("\n2. Eliminate subjects")
        # if multiple subject combinations exist, double list
        if 'AP option' in user_kb.keys():
            subjects_from = 'AP'
        elif user_kb['diplomas'] == 'IB':
            subjects_from = 'IB'
        if any(isinstance(subjComb, list) for subjComb in study[subjects_from]):
            print("nested subject combinations")
            match = 0
            for subjOptionN in study[subjects_from]:
                #print("\nstudy: "+study['label'])
                #print(subjOptionN)
                #print("in user: ")
                #print(user_kb['subjects'])
                if set(subjOptionN) == set(user_kb['subjects']) or set(subjOptionN).issubset(set(user_kb['subjects'])):  
                    # if match, don't check rest and return for next study
                    match = 1
                    print("*** found match")
                    #break
            if match == 0: # if no match found when loop is complete, remove study
                studies_kb.remove(study)
                print("xxx removed: ")
                #print(study['label'])
                #print("{} studies left\n".format(len(studies_kb)))       
        else:
            print("non-nested subjected combinations")
            for studySubjs in study[subjects_from]:
                #print("\nstudy: "+study['label'])
                #print(studySubjs)
                #print("in user: ")
                #print(user_kb['subjects'])
                if studySubjs not in user_kb['subjects']:
                    #print("{} not in user_kb['subjects']".format(studySubjs))
                    studies_kb.remove(study)
        return

    if 'subjectGrades' in visited and user_kb['subjectGrades'] != []:
        print("\n3. Eliminating grade")
        print("in visited, the subject is: " + visited[1])
        # if user grade > study-subject max grade, try again
        #print("user's grade")
        print(user_kb['subjectGrades'][0])
        print("study "+study['label'])
        #print(study[visited[1]][0])
        # if user grade < study-subject min grade
        if visited[1] in study.keys():
            print(visited[1] + "subject exists")
        if visited[1] in study.keys() and user_kb['subjectGrades'][0] < int(study[visited[1]][0]):
            print("xxx removing study "+study['label'])
            studies_kb.remove(study) 
        return

    # matching english level
    if 'english level' in visited and user_kb['english level'] != []:
        print("Eliminating English level")
        if user_kb['english level'] not in study['english level']:
            studies_kb.remove(study)
        return

    # matching english level grades
    if 'check english grades' in visited:
        print("Eliminating English Grades")
        study_eng_grd = study[user_kb['english level']]
        usr_eng_grd = user_kb['english grades']
        print("english grades: " + str(usr_eng_grd))
        for i in range(len(usr_eng_grd)):
            print(usr_eng_grd[i])
            print(study_eng_grd[i][1])
            if int(usr_eng_grd[i]) < int(study_eng_grd[i][1]):
                studies_kb.remove(study)
                print("removed "+str(study['label']))
                return
    
    print("\njust returning\n")
    return

'''
    # matching subjects
    if 'subjects' in user_kb.keys() and user_kb['subjects'] != [] and 'subjectGrades' in user_kb.keys() and user_kb['subjectGrades'] == []:
        # True if nested lists, means subjects have grades
        if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]):
            #print("\nIn elimination, subjects are known to have grades")
            for subject in study[user_kb['diplomas']]:
                #print("\nnow in study {}".format(study['label']))
                #print("?will check if subjectGrade {} in study is in student's subject {}?".format(subject, user_kb['subjects']))
                if subject[0] not in user_kb['subjects']:
                    #print("  subjectGrade {} in study is NOT in student's subject {}".format(subject, user_kb['subjects']))
                    studies_kb.remove(study)
                    #print("{} studies left\n".format(len(studies_kb)))
                    return
        # subjects do NOT have grades in study
        else:
            for subject in study[user_kb['diplomas']]:
                if subject not in user_kb['subjects']:
                    studies_kb.remove(study)
                    return

    if 'subjectGrades' in user_kb.keys() and user_kb['subjectGrades'] != []:
        #print("\nMatching grades")
        for subjGrad in study[user_kb['diplomas']]:
            if subjGrad[0] == user_kb['subjectGrades'][0][0]:
                if int(user_kb['subjectGrades'][0][1]) < subjGrad[1]:
                    studies_kb.remove(study)
                    return
            
    # matching english level
    if 'english level' in user_kb.keys():
        if user_kb['english level'] is not None and user_kb['english level'] not in study['english level']:
            studies_kb.remove(study)
            return

    # matching english level grades
    if ('english level' in user_kb.keys() and user_kb['english level'] is not None and 'english grades' in user_kb.keys() 
            and user_kb['english grades'] and user_kb['english level'] in study.keys()):
        study_eng_grd = study[user_kb['english level']]
        usr_eng_grd = user_kb['english grades']
        for i in range(len(usr_eng_grd)):
            if (len(usr_eng_grd[i]) > 1 and len(study_eng_grd[i]) > 1 and
                    usr_eng_grd[i][0] == study_eng_grd[i][0] and usr_eng_grd[i][1] < study_eng_grd[i][1]):
                studies_kb.remove(study)
                return
'''