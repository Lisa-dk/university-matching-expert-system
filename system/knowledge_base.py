class KnowledgeBase():
    def __init__(self) -> None:
        self.kb = get_kb_dict()
    
    def get_kb_dict():
        kb = [
            {
                'label': 'Chemical Engineering and Chemistry',
                'university': 'Technical University of Eindhoven',
                'subjects': ['mathematics, physics, chemistry'],
                'english level': [('TOEFL', 90, 21), ('IELTS', 6.5, 6.0), ('CPE', 180, 169), ('CPA', 176, 169), 'IB English programme', ('IB A HL', 5)]
            },
            {
                'label': 'Electrical Engineering',
                'university': 'Technical University of Eindhoven',
                'subjects': ['mathematics, physics'],
                'english level': [('TOEFL', 90, 21), ('IELTS', 6.5, 6.0), ('CPE', 180, 169), ('CPA', 176, 169), 'IB English programme', ('IB A HL', 5)]
            },

        ]