from enum import Enum


class QuestionType(Enum):
    SELECT = 1
    MULTI_SELECT = 2
    TEXT_FIELD = 3


class Question:
    def __init__(self):
        # global question_options
        self.question_options = {}
        self.create_options_dict()

        # self.questions = ["Do you know what you want to study? (yes/no)"]
        self.questions = [
            ["Do you know what you want to study?", QuestionType.SELECT, self.question_options.get('yes-no question')]]
        # self.questions = ["----> What is your high school diploma?"]

    def create_options_dict(self):
        self.question_options = {
            # TODO: entrance exam question needs 'no' - 'no preference'
            'yes-no question': ['yes', 'no'],
            'yes-no_preference question': ['yes', 'no preference'],
            'no-no_preference question': ['no', 'no preference'],
            'preferences': ['Chemistry', 'Biology', 'Mathematics', 'Physics', 'Electricity', 'Magnetism',
                            'Material Science', 'Architecture', 'Building Sciences', 'Real Estate', 'Transport',
                            'Cars', 'Electronics', 'Software', 'Climate', 'Economics', 'Social Sciences', 'Business',
                            'Management', 'Production', 'Information Systems', 'Programming', 'Internet', 'Psychology',
                            'Robots', 'Technology', 'Design', 'Innovation', 'Society', 'Environment', 'Sustainability',
                            'Healthcare', 'Creativity', 'Chemical Engineering', 'Electrical Engineering',
                            'Process Engineering', 'Automative Technology', 'Mechanical Engineering',
                            'Industrial Engineering', 'Computer Science', 'Biomedical Engineering',
                            'Circular Engineering', 'Aerospace', 'Data Processing', 'Civil Engineering',
                            'Graphic Design', 'Marketing', 'Business Engineering', 'Technical'],
            'diploma': ['IB', 'Lise Diploma', 'Abitur', 'Label France Education'],
            # 'courses': ['Analysis and Approaches SL', 'Analysis and Approaches HL', 'Mathematics SL', 'Mathematics HL', 'Calculus', 'Physics SL', 'Physics HL', 'Chemistry SL', 'Chemistry HL'],  # TODO: This one is not used
            'subjects IB': ['Analysis and Approaches HL', 'Mathematics HL', 'Mathematics SL', 'Physics HL', 'Physics SL',
                            'Chemistry HL', 'Chemistry SL', 'Biology HL', 'Biology SL', 'English HL', 'English SL',
                            'None of the above'],
            'subjects AP': ['Calculus A/B', 'Calculus B/C', 'Physics 1', 'Physics 2', 'Physics C Mechanics',
                            'Physics C Electricity and Magnetism', 'Chemistry', 'None of the above'],
            'cities': ['Eindhoven', 'Groningen', 'Maastricht', 'Delft', 'Enschede', "no preference"],
            'cities 2': ['Eindhoven', 'Groningen', 'Maastricht', 'Delft', 'Enschede', "no preference"],
            'English test': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'None of the above']
        }

    def get_question_options(self, key):
        return self.question_options.get(key)

    def get_questions(self):
        return self.questions

    def get_current_question(self):
        return self.questions[0]

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        self.questions.remove(question)
        # self.questions.pop(0)

    def clear_question(self):
        self.questions.clear()

    def get_question_list_len(self):
        return len(self.questions)
