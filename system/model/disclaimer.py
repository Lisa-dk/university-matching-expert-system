class Disclaimer:
    def __init__(self):
        self.disclaimer = ''
        self.disclaimers = ''

    def getCurrentDisclaimer(self):
        return self.disclaimer
    
    def get_disclaimers(self):
        return self.disclaimers

    def addDisclaimer(self, disclaimer):
        self.disclaimer = disclaimer
        self.disclaimers += disclaimer

    def resetCurrentDisclaimer(self):
        self.disclaimer = ''

    def checkDisclaimer(self):
        if self.disclaimer != '':
            return True
