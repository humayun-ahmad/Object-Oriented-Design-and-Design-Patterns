class EuropeanSocket:
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

class AmericanSocket:
    def voltage(self):
        return 120

    def live(self):
        return 1

    def neutral(self):
        return -1