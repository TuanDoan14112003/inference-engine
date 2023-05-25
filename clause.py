
class Clause:
    """
    This class is used to represent a propositional logic clause with the following fields:
    right: the right clause
    left: the left clause
    operator: the logic operator
    """
    def __init__(self, *, right, left=None, operator=None): # * is used to force keyword argument
        self.satisfied = False
        self.left = left
        if operator:
            self.operator = operator.strip() # remove any whitespace
        else:
            self.operator = None
        self.right = right

    def setPropositionalSymbol(self, model):
        """
        Given a model, this function will assign values to the right and left clauses
        """
        if self.left: # check if self.left is not None
            self.left.setPropositionalSymbol(model)
        self.right.setPropositionalSymbol(model)

    def getValue(self):
        """
        This function will return the value (T/F) of the clause based on the operator
        """
        if self.left is None and self.operator is None: # if the clause is made up of a single symbol
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
        """
        This function will return the total number of operands of the clause
        """
        return self.right.getNumberOfOperands() + (self.left.getNumberOfOperands() if self.left else 0)

    def __str__(self):
        """Return the string representation of the clause"""
        return ("(" if self.operator else "") + (str(self.left) if self.left else "") + (
            self.operator if self.operator else "") + str(self.right) + (")" if self.operator else "")

    def __eq__(self, other):
        """
        This function will compare 2 clauses
        """
        if not isinstance(other,Clause):
            return False
        return self.left == other.left and self.right == other.right and self.operator == other.operator

    def __hash__(self):
        return hash(str(self))


if __name__ == "__main__":
    """Testing"""
    from propositionalSymbol import PropositionalSymbol
    from generalLogicParser import parseClause
    symbolA = PropositionalSymbol("A")
    symbolB = PropositionalSymbol("B")
    symbolC = PropositionalSymbol("C")
    clauseAAndB = Clause(left = symbolA, operator= "&", right = symbolB)
    clauseTotal = Clause(left = clauseAAndB,operator = "<=>", right=symbolC)
    clauseTotal.setPropositionalSymbol([PropositionalSymbol("A", True), PropositionalSymbol("B", True), PropositionalSymbol("C",True)])
    print(clauseTotal.getValue())
    print(parseClause("a & a & c & d  => b").getNumberOfOperands())
