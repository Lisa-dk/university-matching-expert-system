def elimination_update(study, studies_kb, user_kb, visited):
    """
    Eliminates studies from the kb through if-then rules.
    :param study: a study in the kb
    :param studies_kb: the kb containing all studies
    :param user_kb: kb containing user info
    :param visited: questions that have passed
    :return: study if it has been eliminated, else 1
    """

    # study preference selection
    if 'study preference' in user_kb.keys() and 'study preference' in visited:

        if not any(item in study['about'] for item in user_kb['study preference']):
            studies_kb.remove(study)
            return study

    # match diplomas
    if 'diplomas' in visited:
        if user_kb['diplomas'] not in study['diplomas']:
            studies_kb.remove(study)
            return study

    # eliminate all if no AP
    if 'None' in visited:
        studies_kb.remove(study)
        return study

    # match subjects
    if 'subjects' in visited:
        if 'AP courses' in user_kb.keys() and user_kb['AP courses'] == 'yes':  # meaning multiple combinations exists
            if 'AP courses' in study.keys() and study['AP courses'] == 'no':
                studies_kb.remove(study)
                return study
            subjects_from = 'AP'
        elif user_kb['diplomas'] == 'IB':
            subjects_from = 'IB'
        # else:
        #     subjects_from = None

        if any(isinstance(subjComb, list) for subjComb in
               study[subjects_from]):  # if subjComb exists, they are found as nested-list structure
            if not any((set(subjOptionN) == set(user_kb['subjects']) or set(subjOptionN).issubset(
                    set(user_kb['subjects']))) for subjOptionN in study[subjects_from]):
                studies_kb.remove(study)
                return study
        else:
            if any(studySubj not in user_kb['subjects'] for studySubj in study[subjects_from]):
                studies_kb.remove(study)
                return study

    # match subject-grade
    if 'subject grades' in visited and len(visited) == 2 and user_kb['subject grades'] != []:  # check if subject is in study

        # if subject is in study and user's subject-grade < study-subject min grade
        if visited[1] in study.keys() and user_kb['subject grades'][0] < int(study[visited[1]]):
            studies_kb.remove(study)

            return study

    # match english test
    if 'english tests' in visited and user_kb['english tests'] != []:
        if user_kb['english tests'] not in study['english tests']:
            studies_kb.remove(study)

            return study

    # match english level grades
    if 'check english grades' in visited:
        study_eng_grd = study[user_kb['english tests']]
        usr_eng_grd = user_kb['english grades']
        for sect in range(len(study[user_kb['english tests']])):
            if float(usr_eng_grd[sect]) < float(study_eng_grd[sect][1]):  # if section in study and grade valid
                studies_kb.remove(study)
                return study

    if 'city' in visited:
        if not any(city in study['city'] for city in
                   user_kb['city']):  # if it is not the case that any city in user_kb is equal to the city of study
            studies_kb.remove(study)
            return study

    # matching multidisciplinary
    if 'multidisciplinary' in visited:
        if study['multidisciplinary'] != 'yes':
            studies_kb.remove(study)

            return study
    
    # matching research
    if 'research' in visited:
        # remove if the study does not offer research
        if study['research'] != 'yes':
            studies_kb.remove(study)
            return study

    # matching practical-oriented approach
    if 'practical oriented' in visited:
        # remove if the study does not offer research
        if study['practical oriented'] != 'yes':
            studies_kb.remove(study)
            return study

    # matching project oriented approach
    if 'project oriented' in visited:
        # remove if the study does not offer research
        if study['project oriented'] != 'yes':
            studies_kb.remove(study)
            return study

    # matching entrance exam
    if 'entrance exam' in visited:
        # remove studies that have entrance exam
        if study['entrance exam'] == 'yes':
            studies_kb.remove(study)
            return study

    # matching study choice check
    if 'study choice check' in visited:
        # remove if the study does not offer study choice check
        if study['study choice check'] != 'yes':
            studies_kb.remove(study)
            return study
    
    # matching numerus fixus
    if 'numerus fixus' in visited:
        # remove studies that are numerus fixus
        if study['numerus fixus'] == 'yes':
            studies_kb.remove(study)
            return study

    return 1
