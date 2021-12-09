from knowledge_base import KnowledgeBase
from questions import QuestionType
from system.rules import rules_check

facts = {}

def forward_chaining(kb):
    questions = [QuestionType.SUBJECT]
    while len(questions) != 0:
        question = questions[0]
        response = input(question)
        facts[question] = response
        
        for item in kb:
            match, next_question = rules_check()
            questions.append(next_question)
            if match:
                kb.remove(item)

            
    questions.remove(question)
    pass

def main():
    kb = KnowledgeBase().kb
    forward_chaining(kb)


if __name__ == "__main__":
    main()