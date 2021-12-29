from model.questions import Question
from model.disclaimer import Disclaimer
from model.rules.user_rules import make_user_kb
from model.rules.elimination_rules import elimination_update
from model.rules.user_rules import make_user_kb


class InferenceEngine:
    def __init__(self, kb):
        self.kb = kb
        self.user_kb = {}
        self.question = Question()
        self.disclaimer = Disclaimer()
        self.setQuestion()
        self.response = None
        self.visited = []

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
            elimination_update(self.kb[i], self.kb, self.user_kb, self.visited)
            # After removal, the items are moved to a lower index in the list.
            if len(self.kb) < size_kb:
                size_kb -= 1
                i -= 1
            i += 1

    def forward_chaining(self):
        self.setQuestion()

        # fc while there are questions to ask
        while len(self.question_list) != 0:
            question = self.getCurrentQuestion()
            response = input("\n" + question + "\n")
            
            # Processing the user information and getting next questions
            make_user_kb(response, self.question, self.disclaimer, self.kb, self.user_kb, self.visited)
            #self.question.removeQuestion(self.currentQuestion)
            self.question.removeQuestion()
            if len(self.question_list) != 0:
                self.setQuestion()
            print("\n**** NEXT QUESTION:" )
            print(self.question_list) 
            print("\n")
            
            #print("entering elim..")
            # Removing studies that don't match

            if self.disclaimer.checkDisclaimer():
                disclaimer = self.disclaimer.getCurrentDisclaimer()
                print("\n" + disclaimer + "\n")
                self.disclaimer.resetCurrentDisclaimer()
            
            self.eliminate_studies()
            print(len(self.kb))

            if len(self.kb) == 0:
                print("No study requirements met.")
                break

        if len(self.kb) > 0 or self.question.endProgram() == 'end': #len(self.question_list) == 0 or len(self.visited) == 0:
            print("Requirements met for the following studies:")
            for study in self.kb:
                print(study['label'] + " at " + study['university'])