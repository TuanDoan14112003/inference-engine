import generalLogicParser as glp
from propositionalSymbol import PropositionalSymbol
from clause import Clause
from copy import deepcopy


class ResolutionAlgorithm:
    def __init__(self, clauses, kb):
        self.clauses = clauses
        self.kb = kb

    def resolve(self, clause1, clause2):
        # if clause1 == clause2:
        #     return
        # if clause1.right == None:
        #     return clause2
        # if clause2.right == None:
        #     return clause1
        if (clause1.operator == "~" or clause2.operator == "~") and clause1.right == clause2.right and clause1.left == clause2.left:
            return None
        # if clause1.operator == "~":
        #     if clause1[1:] in clause2:
        #         return clause2.replace(clause1[1:], "")
        # if clause2.operator == "~":
        #     if clause2[1:] in clause1:
        #         return clause1.replace(clause2[1:], "")
        clause = Clause(left=clause1, operator="&", right=clause2)
        clauseOuter = deepcopy(clause)
        clauseInner = deepcopy(clause)
        while (isinstance(clauseOuter.left.right, PropositionalSymbol)):
            while (isinstance(clauseInner.left.right, PropositionalSymbol)):
                if clauseOuter.right == clauseInner.right:
                    return None
                else:
                    clauseInner = clauseInner.left
            clauseOuter = clauseOuter.left
        return clause

    def resolution(self):
        new = []
        for i in range(len(self.clauses)):
            for j in range(i+1, len(self.clauses)):
                if self.resolve(self.clauses[i], self.clauses[j]) == None:
                    return True
                new.append(self.resolve(self.clauses[i], self.clauses[j]))
                if self.resolve(self.clauses[i], self.clauses[j]) == None:
                    return True
                if new in self.clauses:
                    return False
                self.clauses += new
