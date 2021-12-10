class KnowledgeBase():
    def __init__(self) -> None:
        self.kb = self.get_kb_dict()
    
    def get_kb_dict(self):
        kb = [
            {
                'label': 'Chemical Engineering and Chemistry',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'subjects': ['chemistry', 'mathematics', 'physics'],
                'english test': ['TOEFL', 'IELTS', 'CPE', 'CPA', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CPA overall' : 176,
                'CPA min': 196,
                'IB A HL overall': 5
            },
            {
                'label': 'Electrical Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Regular Lise Diploma', 'AP', 'IB', 'Label France Educaiton', 'British GCE A Levels'],
                'subjects': ['mathematics', 'physics'],
                'english test': ['TOEFL', 'IELTS', 'CPE', 'CPA', 'IB English programme', 'IB A HL'],
                'TOEFL overall': 90,
                'TOEFL min': 21,
                'IELTS overall': 6.5,
                'IELTS min': 6.0,
                'CPE overall' : 180,
                'CPE min': 169,
                'CPA overall' : 176,
                'CPA min': 196,
                'IB A HL overall': 5
            }
        ]
        return kb
