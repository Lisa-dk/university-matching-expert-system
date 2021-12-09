def elimination_update(study, studies_kb, user_kb):
    for subject in study['subjects']:
        if subject not in user_kb['subjects']:
            studies_kb.remove(study)
            return 
    
    if user_kb['english test'] != None and user_kb['english test'] not in study['english test']:
        studies_kb.remove(study)
        return
    
    if (user_kb['english test'] != None and user_kb[(user_kb['english test'] + 'overall')] != '' and
                user_kb[(user_kb['english test'] + 'overall')] in user_kb.keys() and 
                user_kb[(user_kb['english test'] + 'overall')] in study.keys() and 
                user_kb[(user_kb['english test'] + 'overall')] < study[user_kb[(user_kb['english test'] + 'overall')]]):
        studies_kb.remove(study)
        return

    
    if (user_kb['english test'] != None and user_kb[(user_kb['english test'] + 'min')] != '' and
                user_kb[(user_kb['english test'] + 'min')] in user_kb.keys() and 
                user_kb[(user_kb['english test'] + 'min')] in study.keys() and 
                user_kb[(user_kb['english test'] + 'min')] < study[user_kb[(user_kb['english test'] + 'min')]]):
        studies_kb.remove(study)
        return
    

