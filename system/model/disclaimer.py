class Disclaimer():
    def __init__(self):
        self.disclaimer = ''

    def getCurrentDisclaimer(self):
        return self.disclaimer

    def addDisclaimer(self, disclaimer):
        self.disclaimer = disclaimer

    def resetCurrentDisclaimer(self):
        self.disclaimer = ''

    def checkDisclaimer(self):
        if self.disclaimer != '':
            return True

