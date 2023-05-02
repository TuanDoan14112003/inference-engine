class PropositionalSymbol:
    def __init__(self,symbol, value):
        self.value = value
        self.symbol = symbol

    def getValue(self):
        return self.value