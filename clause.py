#define clause class
class Clause:
    def __init__ (self, left, operator = None, right = None):
        self.satisfied = False
        self.left = left
        if operator:
            self.operator = operator.strip()
        else:
            self.operator = None
        self.right = right
        self.value = None
    
    # def setValue(self, value):
    #     self.value = value
    def setPropositionalSymbol(self, propositionalSymbolList):
        self.left.setPropositionalSymbol(propositionalSymbolList)
        if self.right:
            self.right.setPropositionalSymbol(propositionalSymbolList)
        


    def getValue(self):
        if self.operator == None:
            return self.left.getValue()
        else:
            if self.operator == "&":
                return self.left.getValue() and self.right.getValue()
            elif self.operator == "=>":
                return (not self.left.getValue()) or self.right.getValue()
            elif self.operator == "||":
                return self.left.getValue() or self.right.getValue()
            elif self.operator == "<=>":
                return self.left.getValue() == self.right.getValue()
            elif self.operator == "~":
                return not self.left.getValue()

    def __str__(self):
        return ("(" if self.right else "")  + str(self.left) + (self.operator if self.operator else "") + (str(self.right) if self.right else "") + (")" if self.right else "")
            
if __name__ == "__main__":
    from propositionalSymbol import PropositionalSymbol
    symbolA = PropositionalSymbol("A", False)
    symbolB = PropositionalSymbol("B", True)
    symbolC = PropositionalSymbol("C", False)
    clauseAAndB = Clause(symbolA , "&", symbolB)
    clauseTotal = Clause(clauseAAndB, "=>", symbolC)
    print(clauseTotal.getValue())
        



    

    


    