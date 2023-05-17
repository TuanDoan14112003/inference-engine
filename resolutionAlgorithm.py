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

        # print(clauses)
        new = set()
        while True:
            clauseList = [list(clause) for clause in clauses]
            print(len(clauseList))
            for i in range(len(clauseList)-1):
                for j in range(i+1,len(clauseList)):
                    # resolvents = self.inferByResolution(clauseList[i],clauseList[j])
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



    def inferByResolution(self,Ci,Cj):
        resolvents = []
        toBeRemovedCi = []
        toBeRemovedCj = []
        for literal in Ci:
            if literal[0] != "~" and (("~" + literal) in Cj):
                # result = [symbol for symbol in Ci if symbol != literal]
                # result.extend([symbol for symbol in Cj if symbol != ("~" + literal)])
                # resolvents.append(result)
                toBeRemovedCi.append(literal)
                toBeRemovedCj.append("~"+literal)

            elif literal[0] == "~" and literal[1:] in Cj:
                # result = [symbol for symbol in Ci if symbol != literal]
                # result.extend([symbol for symbol in Cj if symbol != literal[1:]])
                # resolvents.append(result)
                toBeRemovedCi.append(literal)
                toBeRemovedCj.append(literal[1:])

        if toBeRemovedCi or toBeRemovedCj:
            result = [symbol for symbol in Ci if symbol not in toBeRemovedCi]
            result.extend([symbol for symbol in Cj if symbol not in toBeRemovedCj])
            resolvents.append(result)
        else:
            resolvents.append(Ci.copy())
            resolvents.append(Cj.copy())
        return resolvents





if (__name__ == "__main__"):
    "b&i => b; b&f => a;"
    from generalLogicParser import parseClause
    # from environment import Environment
    # env = Environment()
    # env.readFile("UnitTest/testcases/horns/horn8.txt")
    # resolution = Resolution()
    # print(resolution.solve(env.knowledgeBase,env.query))
    # print(resolution.inferByResolution(["a","b","c"],["~a","~b","c"]))

    resolution = Resolution()
    clause1 = parseClause("h&h => h")
    clause2 = parseClause("h")
    # clause3 = parseClause("b")
    query = parseClause("h")
    print(resolution.solve(kb=[clause1,clause2],query=query))




