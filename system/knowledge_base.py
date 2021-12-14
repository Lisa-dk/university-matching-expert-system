class KnowledgeBase():
    def __init__(self) -> None:
        self.kb = self.get_kb_dict()
    
    def get_kb_dict(self):
        kb = [
            {
                'label': 'Chemical Engineering and Chemistry',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL', 'Physics HL', 'Chemistry HL'], 
                'AP': [['Calculus', 3], ['Physics', 3], ['Chemistry', 3]],
                'Lise Diploma': [['Mathematics', 75], ['Physics', 75], ['Chemistry', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Electrical Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL', 'Physics HL'],
                'AP': [['Calculus', 3], ['Physics', 3]],
                'Lise Diploma': [['Mathematics', 75], ['Physics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Architecture, Urbanism and Building',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL', 'Physics HL'],
                'AP': [['Calculus', 3], ['Physics', 3]],
                'Lise Diploma': [['Mathematics', 75], ['Physics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Computer Science and Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL'],
                'AP': [['Calculus', 3]], 
                'Lise Diploma': [['Mathematics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Psychology & Technology',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL'],
                'AP': [['Calculus', 3]], 
                'Lise Diploma': [['Mathematics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Automative Techonology',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL', 'Physics HL'],
                'AP': [['Calculus', 3], ['Physics', 3]],
                'Lise Diploma': [['Mathematics', 75], ['Physics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Mechanical Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL', 'Physics HL'],
                'AP': [['Calculus', 3], ['Physics', 3]],
                'Lise Diploma': [['Mathematics', 75], ['Physics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Sustainable Innovation',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France Education', 'British GCE A Levels'],
                'IB': ['Mathematics HL'],
                'AP': [['Calculus', 3]], 
                'Lise Diploma': [['Mathematics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
            {
                'label': 'Industrial Engineering',
                'university': 'Technical University of Eindhoven',
                'diplomas': ['Lise Diploma', 'AP', 'IB', 'Label France education', 'British GCE A Levels'],
                'IB': ['Mathematics HL'],
                'AP': [['Calculus', 3], ['Physics', 3]],
                'Lise Diploma': [['Mathematics', 75], ['Physics', 75]],
                'english level': ['TOEFL iBT', 'IELTS (academic)', 'CPE', 'CAE', 'IB English programme', 'IB A HL'],
                'TOEFL iBT': [['overall', 90], ['Reading', 21], ['Listening', 21], ['Speaking', 21], ['Writing', 21]],
                'IELTS (academic)': [['overall', 6.5], ['Reading', 6.0], ['Listening', 6.0], ['Speaking', 6.0], ['Writing', 6.0]],
                'CPE' : [['overall', 180], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'CAE' : [['overall', 176], ['Reading', 169], ['Listening', 169], ['Speaking', 169], ['Writing', 169]],
                'IB A HL': [['overall', 5]]
            },
        ]
        return kb
