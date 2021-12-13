def elimination_update(study, studies_kb, user_kb):

    # matching diplomas
    if user_kb['diplomas'] not in study['diplomas']:
        studies_kb.remove(study)
        return
    
    # matching subjects
    if 'subjects' in user_kb.keys() and user_kb['subjects'] != []:
        # True if nested lists, means subjects have grades
        if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]): 
            for subject in study[user_kb['diplomas']]:
                if subject[0] not in user_kb['subjects']:
                    studies_kb.remove(study)
                    return   
        # subjects do NOT have grades in study 
        else:
            print("study has NO grades")
            print(study[user_kb['diplomas']])
            for subject in study[user_kb['diplomas']]:
                if subject not in user_kb['subjects']:
                    studies_kb.remove(study)
                    return 

    # matching grades
    if 'subjectGrades' in user_kb.keys() and user_kb['subjectGrades'] != []:
        i=0
        for subject in study[user_kb['diplomas']]:
            if int(user_kb['subjectGrades'][i][1]) < subject[1]  :
                studies_kb.remove(study)
                return 
            i+=1

    # matching english level
    if 'english level' in user_kb.keys():
        if user_kb['english level'] != None and user_kb['english level'] not in study['english level']:
            studies_kb.remove(study)
            return
        
        # matching english level overall score
        if (user_kb['english level'] != None and user_kb[(user_kb['english level'] + ' overall')] != '' and
                    user_kb[(user_kb['english level'] + 'overall')] in user_kb.keys() and 
                    user_kb[(user_kb['english level'] + 'overall')] in study.keys() and 
                    user_kb[(user_kb['english level'] + 'overall')] < study[user_kb[(user_kb['english level'] + 'overall')]]):
            studies_kb.remove(study)
            return

        # matching english level minimum score
        if (user_kb['english level'] != None and (user_kb['english level'] + 'min') in user_kb.keys() and
                    user_kb[(user_kb['english level'] + 'min')] != '' and
                    user_kb[(user_kb['english level'] + 'min')] in user_kb.keys() and 
                    user_kb[(user_kb['english level'] + 'min')] in study.keys() and 
                    user_kb[(user_kb['english level'] + 'min')] < study[user_kb[(user_kb['english level'] + 'min')]]):
            studies_kb.remove(study)
            return
        

