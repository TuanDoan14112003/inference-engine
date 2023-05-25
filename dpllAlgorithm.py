from clause import Clause
from generalLogicParser import convertToCNF
from copy import deepcopy
import random
class DPLLAlgorithm:
    def solve(self,kb,query):
        cnfClausesList = []
        for clause in kb:
            cnfClausesList.append(convertToCNF(clause))
        negationOfQuery = Clause(operator="~",right=query)
        cnfClausesList.append(convertToCNF(negationOfQuery))
        cnfClausesList = [str(clause).replace("(","").replace(")","") for clause in cnfClausesList]
        clauses = []
        for clause in cnfClausesList:
            for disjunctionOfSymbol in clause.split("&"):
                clauses.append(disjunctionOfSymbol)

        clauses = [clause.split("||") for clause in clauses]
        clauses = {frozenset(clause) for clause in clauses}
        return not self.dpll(clauses)
    def dpll(self,formula):
        if formula == set():
            return True
        if frozenset() in formula:
            return False
        for clause in formula:
            if len(clause) == 1:
                return self.dpll(self.symplify(formula,list(clause)[0]))
        literal = random.choice(random.choice([list(clause) for clause in formula]))
        if self.dpll(self.symplify(formula,literal)):
            return True
        else:
            if literal[0] == "~":
                negationLiteral = literal[1:]
            else:
                negationLiteral = "~" + literal
            return self.dpll(self.symplify(formula,negationLiteral))


    def symplify(self,formula,literal):
        newFormula = set()
        for clause in formula:
            if literal in clause:
                continue
            if literal[0] != "~" and "~" + literal in clause:
                newFormula.add(frozenset({subClause for subClause in clause if subClause != ("~" + literal)}))
            elif literal[0] == "~" and literal[1:] in clause:
                newFormula.add(frozenset({subClause for subClause in clause if subClause != literal[1:]}))
            else:
                newFormula.add(frozenset({subClause for subClause in clause}))

        return newFormula




if __name__ == "__main__":
    t = DPLLAlgorithm()
    from generalLogicParser import parseClause
    from environment import Environment
    env = Environment()
    env.readFile("file.txt")
    dpll = DPLLAlgorithm()
    print(dpll.solve(env.knowledgeBase,env.query))
    print()


    # dpll = DPLLAlgorithm()
    # clause1 = parseClause("~a")
    # clause2 = parseClause("a")
    # query = parseClause("b")
    # print(dpll.solve(kb=[clause1,clause2],query=query))

    # formula = {frozenset({'a'}), frozenset({'~a'}), frozenset({'~b'})}
    # dpll = DPLLAlgorithm()
    # print(dpll.symplify(formula,"a"))






