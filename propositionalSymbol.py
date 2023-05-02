class PropositionalSymbol:
    def __init__(self, symbol):
        self.symbol = symbol.strip()
        self.value = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        return self.symbol == other.symbol
