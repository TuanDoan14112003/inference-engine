from clause import Clause
from generalLogicParser import convertToCNF
class Resolution:
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
        print(clause)
        new = set()
        while True:
            clauseList = [list(clause) for clause in clauses]

            for i in range(len(clauseList)-1):
                for j in range(i+1,len(clauseList)):
                    resolvents = []
                    canBeResolved = False
                    for literal in clauseList[i]:
                        if literal[0] != "~" and (("~"+ literal) in clauseList[j]):
                            result = [symbol for symbol in clauseList[i] if symbol != literal]
                            result.extend([symbol for symbol in clauseList[j] if symbol != ("~" + literal)])
                            resolvents.append(result)
                            canBeResolved = True

                        elif literal[0] == "~" and literal[1:] in clauseList[j]:
                            result = [symbol for symbol in clauseList[i] if symbol != literal]
                            result.extend([symbol for symbol in clauseList[j] if symbol != literal[1:] ])
                            resolvents.append(result)
                            canBeResolved = True
                    if not canBeResolved:
                        resolvents.append(clauseList[i].copy())
                        resolvents.append(clauseList[j].copy())
                    if [] in resolvents:
                        return True

                    resolventsSet = {frozenset(clause) for clause in resolvents}
                    new = new.union(resolventsSet)

            if new.issubset(clauses):
                return False
            clauses = clauses.union(new)






if (__name__ == "__main__"):
    "b&i => b; b&f => a;"
    from generalLogicParser import parseClause
    from environment import Environment
    env = Environment()
    env.readFile("file.txt")
    resolution = Resolution()
    print(resolution.solve(env.knowledgeBase,env.query))


    # resolution = Resolution()
    # clause1 = parseClause("a&b&c&d&e => f")
    # clause2 = parseClause("a")
    # clause3 = parseClause("b")
    # clause4 = parseClause("c")
    # clause5 = parseClause("d")
    # clause6 = parseClause("e")
    # query = parseClause("f")
    # print(resolution.solve(kb=[clause1,clause2,clause3,clause4,clause5,clause6],query=query))




