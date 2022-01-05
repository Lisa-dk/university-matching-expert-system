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
        self.questions = [["Do you know what you want to study?", QuestionType.SELECT, self.question_options.get('yes-no question')]]
        # self.questions = ["----> What is your high school diploma?"]

    def create_options_dict(self):
        self.question_options = {
            'yes-no question': ['yes', 'no'],
            'yes-no_preference question': ['yes', "I don't mind"],
            'preferences': ['Technology', 'Design', 'Innovation', 'Society', 'etc.'],
            'diploma': ['IB', 'Lise Diploma', 'Abitur', 'Label France Education', 'British GCE A Levels'],  # TODO: Do we still use British GCE A Levels?
            'courses': ['Analytics & Approaches SL', 'Analytics & Approaches HL', 'Mathematics SL', 'Mathematics HL',
                        'Calculus', 'Physics SL', 'Physics HL', 'Chemistry SL', 'Chemistry HL'],  # TODO: This one is not used
            'subjects IB': ['Analysis & Approaches', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'English SL', 'English HL'],
            'subjects AP': ['Calculus A/B', 'Calculus B/C', 'Physics 1', 'Physics 2', 'C Mechanics', 'C Electricity and Magnetism', 'Chemistry'],
            'cities': ['Eindhoven', 'Groningen', 'Maastricht', 'Delft', 'Enschede', "I don't mind"],
            'cities 2': ['Eindhoven', 'Groningen', 'Maastricht', 'Delft', "I don't mind"],
            'English test': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE']
        }

    def get_question_options(self, key):
        return self.question_options.get(key)

    def get_questions(self):
        return self.questions

    def getCurrentQuestion(self):
        return self.questions[0]

    def add_question(self, question):
        self.questions.append(question)

    def remove_question(self, question):
        self.questions.remove(question)
        # self.questions.pop(0)

    def clearQuestion(self):
        self.questions.clear()

    def getQuestionListLen(self):
        return len(self.questions)
