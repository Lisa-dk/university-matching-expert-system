from knowledge_base import KnowledgeBase
from questions import Question
from rules import rules_check

user_kb = {}

def forward_chaining(kb):
    queries = Question()
    question_list = queries.getQuestions()
    while len(question_list) != 0:
        question = question_list[0]
        response = input(question + "\n")
        rules_check(response, queries, kb, user_kb)
        queries.removeQuestion(question)
        question_list = queries.getQuestions()


def main():
    kb = KnowledgeBase().kb
    forward_chaining(kb)


if __name__ == "__main__":
    main()