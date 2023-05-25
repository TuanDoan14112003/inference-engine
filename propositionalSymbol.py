class PropositionalSymbol:
    """This class represent a single propositional symbol"""
    def __init__(self, symbol, value = None):
        self.symbol = symbol.strip()
        self.value = value

    def getValue(self):
        return self.value

    def getNumberOfOperands(self):
        return 1

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        return self.symbol == other.symbol
    
    def setPropositionalSymbol(self,model):
        """Given a model, this function will set the correct value (T/F) to the symbol"""
        for symbol in model:
            if self == symbol:
                self.value = symbol.getValue()

            
