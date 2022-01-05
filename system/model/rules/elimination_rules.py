def elimination_update(study, studies_kb, user_kb, visited):
    
    # study preference selection
    if 'study preference' in user_kb.keys() and 'study preference' in visited:
        #print("\nEliminate study preference")

        if not any(item in study['about'] for item in user_kb['study preference']):
            #print("xxx removed: " + str(study['label']))
            studies_kb.remove(study)
        return


    # match diplomas
    if 'diplomas' in visited:
        #print("\n1. Eliminate diplomas")

        if user_kb['diplomas'] not in study['diplomas']:
            studies_kb.remove(study)
            #print("xxx removed: " + str(study['label']))
        return


    # eliminate all if no AP
    if 'None' in visited:
        #print("\n1b. Eliminate all studies")

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

    # match subjects
    if 'subjects' in visited:
        #print("\nEliminate subjects")

        if 'AP courses' in user_kb.keys() and user_kb['AP courses'] == 'yes':  # meaning multiple combinations exists
            if 'AP courses' in study.keys() and study['AP courses'] == 'no':
                studies_kb.remove(study)
                #print("xxx removed: " + str(study['label']))
                return
            subjects_from = 'AP'
        elif user_kb['diplomas'] == 'IB':
            subjects_from = 'IB'

        if any(isinstance(subjComb, list) for subjComb in
               study[subjects_from]):  # if subjComb exists, they are found as nested-list structure
            #print("NESTED subject combinations")
            #print(str(study['label']))
            if not any((set(subjOptionN) == set(user_kb['subjects']) or set(subjOptionN).issubset(
                    set(user_kb['subjects']))) for subjOptionN in study[subjects_from]):
                studies_kb.remove(study)
                #print("xxx removed: " + str(study['label']))
        else:
            #print("NON-nested subjected combinations")
            if any(studySubjs not in user_kb['subjects'] for studySubjs in study[subjects_from]):
                studies_kb.remove(study)
                #print("xxx removed: " + str(study['label']))
        return


    # match subject-grade
    if 'subject grades' in visited and len(visited) == 2 and user_kb[
        'subject grades'] != []:  # check if subject is in study
        #print("\nEliminating grade")
        #print("in visited, the current subject is: " + visited[1])
        #print("user's grade" + str(user_kb['subject grades'][0]))
        #print("for study " + study['label'])

        # print to check if subject is in study
        #print(visited[1] + " is in this study's req.")

        # if subject is in study and user's subject-grade < study-subject min grade
        if visited[1] in study.keys() and user_kb['subject grades'][0] < int(study[visited[1]]):
            studies_kb.remove(study)
            #print("xxx removing study " + study['label'])

        return


    # match english test
    if 'english tests' in visited and user_kb['english tests'] != []:
        #print("Eliminating English level")

        if user_kb['english tests'] not in study['english tests']:
            studies_kb.remove(study)
            #print("xxx removing study " + study['label'])

        return


    # match english level grades
    if 'english grades' in visited:
        #print("Eliminating English Grades")

        study_eng_grd = study[user_kb['english tests']]
        usr_eng_grd = user_kb['english grades']
        #print("user english grades: " + str(usr_eng_grd))
        for sect in range(len(usr_eng_grd)):
            #print("user " + str(usr_eng_grd[sect]))
            #print("study " + str(study_eng_grd[sect][1]))
            if int(usr_eng_grd[sect]) < int(study_eng_grd[sect][1]):
                studies_kb.remove(study)
                #print("xxx removing study " + study['label'])
                return


    if 'city' in visited:
        #print("Eliminating Cities")

        if not any(city in study['city'] for city in
                   user_kb['city']):  # if it is not the case that any city in user_kb is equal to the city of study
            studies_kb.remove(study)
            #print("xxx removing study " + study['label'])
        return

    
    # matching multidisciplinary
    if 'multidisciplinary' in visited:
        #print("\nEliminating Multidisciplinary")
    
        if study['multidisciplinary'] != 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return


    # matching enterance exam
    if 'enterance exam' in visited:
        #print("\nEliminating Enterance Exam")
    
        # remove studies that have enterance exam
        if study['enterance exam'] == 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return


    # matching study choice check
    if 'study choice check' in visited:
        #print("\nEliminating Study Choice Check")

        # remove if the study does not offer study choice check
        if study['study choice check'] != 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return


    # matching research
    if 'research' in visited:
        #print("\nEliminating Research")

        # remove if the study does not offer research
        if study['research'] != 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return


    # matching practical-oriented approach
    if 'practical oriented' in visited:
        #print("\nEliminating Practical Oriented")

        # remove if the study does not offer research
        if study['practical oriented'] != 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return

    
    # matching project oriented approach
    if 'project oriented' in visited:
        #print("\nEliminating Project Oriented")

        # remove if the study does not offer research
        if study['project oriented'] != 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return

    
    # matching numerus fixus
    if 'numerus fixus' in visited:
        #print("\nEliminating Numerus Fixus")
    
        # remove studies that are numerus fixus
        if study['numerus fixus'] == 'yes':  
            studies_kb.remove(study)
            #print("xxx removing study "+study['label'])
        
        return


    #print("return")
    return


'''
GPA?
Preferences:
    Does the client want to have to get the Bachelor's diploma approved in Turkey? (This filters based on the top 600 universities ranking).
'''
