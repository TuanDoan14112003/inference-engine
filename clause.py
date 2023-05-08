# define clause class
class Clause:
    def __init__(self, *, right, left=None, operator=None): #force keyword argument
        self.satisfied = False
        self.left = left
        if operator:
            self.operator = operator.strip()
        else:
            self.operator = None
        self.right = right
        # self.value = None

    # def setValue(self, value):
    #     self.value = value
    def setPropositionalSymbol(self, model):
        if self.left:
            self.left.setPropositionalSymbol(model)
        self.right.setPropositionalSymbol(model)

    def getValue(self):
        if self.left is None and self.operator is None:
            return self.right.getValue()
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
                return not self.right.getValue()

    def getNumberOfOperands(self):
        return self.right.getNumberOfOperands() + (self.left.getNumberOfOperands() if self.left else 0)

    def __str__(self):
        return ("(" if self.operator else "") + (str(self.left) if self.left else "") + (
            self.operator if self.operator else "") + str(self.right) + (")" if self.operator else "")

    def __eq__(self, other):
        if not isinstance(other,Clause):
            return False
        return self.left == other.left and self.right == other.right and self.operator == other.operator

    def __hash__(self):
        return hash(str(self))


if __name__ == "__main__":
    from propositionalSymbol import PropositionalSymbol
    from generalLogicParser import parseClause
    symbolA = PropositionalSymbol("A")
    symbolB = PropositionalSymbol("B")
    symbolC = PropositionalSymbol("C")
    clauseAAndB = Clause(left = symbolA, operator= "&", right = symbolB)
    clauseTotal = Clause(left = clauseAAndB,operator = "<=>", right=symbolC)
    clauseTotal.setPropositionalSymbol([PropositionalSymbol("A", True),PropositionalSymbol("B", True), PropositionalSymbol("C", True)])
    print(parseClause("a&b&c&d&e&g&i => f").left.getNumberOfOperands())
