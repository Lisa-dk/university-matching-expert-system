def elimination_update(study, studies_kb, user_kb):
    # matching diplomas
    if user_kb['diplomas'] not in study['diplomas']:
        studies_kb.remove(study)
        #print("removed: " + study)
        return

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
