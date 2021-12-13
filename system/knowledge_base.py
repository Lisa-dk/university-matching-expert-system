class KnowledgeBase():
    def __init__(self) -> None:
        self.kb = self.get_kb_dict()
    
    def get_kb_dict(self):
        kb = [
            {
                'label': 'Chemical Engineering and Chemistry',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Analysis&ApproachesHL', 'MathematicsHL', 'PhysicsHL', 'ChemistryHL', 'PhysicsSL', 'ChemistrySL'], #note: doesn't work when subject and HL/SL written with space
                'AP': [['CalculusA/B',3], ['CalculusB/C',3], ['Physics1&2',3], ['PhysicsC',3], ['Chemistry',3]], #this-OR-that subjects, not all mandatory... Right now the code expects all to be taken in highschool
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5,
                'disclaimer': 'All subjects must have a min score of 3.',
            },
            {
                'label': 'Electrical Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5], ['physics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3], ['Physics1&2',3], ['PhysicsC',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Architecture, Urbanism and Building',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5], ['physics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3], ['Physics1&2',3], ['PhysicsC',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Computer Science and Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Psychology & Technology',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Automative Techonology',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5], ['physics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3], ['Physics1&2',3], ['PhysicsC',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Mechanical Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5], ['physics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3], ['Physics1&2',3], ['PhysicsC',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Sustainable Innovation',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Industrial Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'IB': [['mathematics',5]],
                'AP': [['CalculusA/B',3], ['CalculusB/C',3], ['Physics1&2',3], ['PhysicsC',3]],
                'english level': ['TOEFL', 'IELTS', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CAE overall' : 176,
                'CAE min': 196,
                'IB A HL overall': 5
            },
        ]
        return kb
