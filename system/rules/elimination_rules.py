def elimination_update(study, studies_kb, user_kb):
    # matching diplomas
    if user_kb['diplomas'] not in study['diplomas']:
        studies_kb.remove(study)
        return

    # matching subjects
    if 'subjects' in user_kb.keys() and user_kb['subjects'] != [] and 'subjectGrades' not in user_kb.keys():
        # True if nested lists, means subjects have grades
        if any(isinstance(subjGrd, list) for subjGrd in study[user_kb['diplomas']]):
            #print("\nin elimination, subjects are known to have grades")
            for subject in study[user_kb['diplomas']]:
                if subject[0] not in user_kb['subjects']:
                    studies_kb.remove(study)
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

        # matching english level overall score
        if (user_kb['english level'] is not None and user_kb[(user_kb['english level'] + ' overall')] != '' and
                user_kb[(user_kb['english level'] + 'overall')] in user_kb.keys() and
                user_kb[(user_kb['english level'] + 'overall')] in study.keys() and
                user_kb[(user_kb['english level'] + 'overall')] < study[
                    user_kb[(user_kb['english level'] + 'overall')]]):
            studies_kb.remove(study)
            return

        # matching english level minimum score
        if (user_kb['english level'] is not None and (user_kb['english level'] + 'min') in user_kb.keys() and
                user_kb[(user_kb['english level'] + 'min')] != '' and
                user_kb[(user_kb['english level'] + 'min')] in user_kb.keys() and
                user_kb[(user_kb['english level'] + 'min')] in study.keys() and
                user_kb[(user_kb['english level'] + 'min')] < study[user_kb[(user_kb['english level'] + 'min')]]):
            studies_kb.remove(study)
            return
