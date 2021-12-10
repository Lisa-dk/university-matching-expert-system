def elimination_update(study, studies_kb, user_kb):

    # matching diplomas
    if user_kb['diplomas'] not in study['diplomas']:
        studies_kb.remove(study)
        return
    
    # matching subjects
    if 'subjects' in user_kb.keys() and user_kb['subjects'] != []:
        for subject in study['subjects']:
            if subject not in user_kb['subjects']:
                studies_kb.remove(study)
                return 
    
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
        

