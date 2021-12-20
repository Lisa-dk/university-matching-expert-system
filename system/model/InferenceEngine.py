from model.questions import Question
from model.rules.question_rules import rules_check
from model.rules.elimination_rules import elimination_update


class InferenceEngine:
    def __init__(self, kb):
        self.kb = kb
        self.user_kb = {}
        self.question = Question()
        self.setQuestion()
        self.response = None

    def setQuestion(self):
        self.question_list = self.question.getQuestions()
        self.currentQuestion = self.question_list[0]

    def getCurrentQuestion(self):
        return self.currentQuestion

    def setRespone(self, response):
        self.response = response

    def eliminate_studies(self):
        size_kb = len(self.kb)
        i = 0
        # Iterating over all studies in the kb and eliminating those
        # which do not match
        while i < size_kb:
            elimination_update(self.kb[i], self.kb, self.user_kb)
            # After removal, the items are moved to a lower index in the list.
            if len(self.kb) < size_kb:
                size_kb -= 1
                i -= 1
            i += 1

    def forward_chaining(self):
        self.setQuestion()

        # fc while there are questions to ask
        while len(self.question_list) != 0:
            print(self.response)
            # Processing the user information and getting next questions
            rules_check(self.response, self.question, self.kb, self.user_kb)
            self.question.removeQuestion(self.currentQuestion)
            self.setQuestion()
            print("entering elim..")
            # Removing studies that don't match
            self.eliminate_studies()
            if len(self.kb) == 0:
                print("No study requirements met.")
                break

        if len(self.kb) > 0:
            print("Requirements met for the following studies:")
            for study in self.kb:
                print(study['label'] + " at " + study['university'])