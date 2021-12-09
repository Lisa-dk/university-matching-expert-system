from knowledge_base import KnowledgeBase
from questions import QuestionType
from system.questions import Question
from system.rules import rules_check

user_kb = {}

def forward_chaining(kb):
    queries = Question()
    question_list = queries.getQuestions()
    while len(question_list) != 0:
        question = question_list[0]
        response = input(question)
        rules_check(response, queries, kb, user_kb)
        queries.removeQuestion(question)
        question_list = queries.getQuestions()

        
    pass

def main():
    kb = KnowledgeBase().kb
    forward_chaining(kb)


if __name__ == "__main__":
    main()