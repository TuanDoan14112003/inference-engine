class PropositionalSymbol:
    def __init__(self, symbol, value = None):
        self.symbol = symbol.strip()
        self.value = value

    # def setValue(self, value):
    #     self.value = value

    def getValue(self):
        if self.value is None:
            raise Exception("Symbol has not been set a value")
        return self.value

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        return self.symbol == other.symbol
    
    def setPropositionalSymbol(self,model):
        for symbol in model:
            if self == symbol:
                self.value = symbol.getValue()

            
