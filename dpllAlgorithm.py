from clause import Clause
from generalLogicParser import convertToCNF
import random
class DPLLAlgorithm:
    def solve(self,kb,query):
        cnfClausesList = []
        for clause in kb:
            cnfClausesList.append(convertToCNF(clause)) # convert clause to cnf
        negationOfQuery = Clause(operator="~",right=query)
        cnfClausesList.append(convertToCNF(negationOfQuery)) # convert negation of query to CNF
        cnfClausesList = [str(clause).replace("(","").replace(")","") for clause in cnfClausesList]
        clauses = []
        for clause in cnfClausesList:
            for disjunctionOfSymbol in clause.split("&"):
                clauses.append(disjunctionOfSymbol)

        clauses = [clause.split("||") for clause in clauses]
        clauses = {frozenset(clause) for clause in clauses} # By making clauses a set, we can remove the duplicate symbols
        return not self.dpll(clauses)
    def dpll(self,formula):
        if formula == set(): # return true if formula has no clause
            return True
        if frozenset() in formula: # return false if formula has an empty clause
            return False
        for clause in formula:
            if len(clause) == 1: # check if there is an unit clause in formula
                return self.dpll(self.simplify(formula,list(clause)[0]))
        literal = random.choice(random.choice([list(clause) for clause in formula])) # choose a random literal in the formula
        if self.dpll(self.simplify(formula,literal)):
            return True
        else:
            if literal[0] == "~":
                negationLiteral = literal[1:]
            else:
                negationLiteral = "~" + literal
            return self.dpll(self.simplify(formula,negationLiteral))


    def simplify(self,formula,literal):
        newFormula = set()
        for clause in formula:
            if literal in clause:
                continue # remove clauses that contains the literal
            # remove the negation of literal in the clauses
            if literal[0] != "~" and "~" + literal in clause:
                newFormula.add(frozenset({subClause for subClause in clause if subClause != ("~" + literal)}))
            elif literal[0] == "~" and literal[1:] in clause:
                newFormula.add(frozenset({subClause for subClause in clause if subClause != literal[1:]}))
            else:
                newFormula.add(frozenset({subClause for subClause in clause}))

        return newFormula




if __name__ == "__main__":
    """Testing"""
    t = DPLLAlgorithm()
    from generalLogicParser import parseClause
    from environment import Environment
    env = Environment()
    env.readFile("file.txt")
    dpll = DPLLAlgorithm()

    # dpll = DPLLAlgorithm()
    # clause1 = parseClause("~a")
    # clause2 = parseClause("a")
    # query = parseClause("b")
    # print(dpll.solve(kb=[clause1,clause2],query=query))

    # formula = {frozenset({'a'}), frozenset({'~a'}), frozenset({'~b'})}
    # dpll = DPLLAlgorithm()
    # print(dpll.simplify(formula,"a"))






