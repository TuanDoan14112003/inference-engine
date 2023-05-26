from clause import Clause
from generalLogicParser import convertToCNF
class Resolution:
    def solve(self,kb,query):
        cnfClausesList = []
        for clause in kb:
            cnfClausesList.append(convertToCNF(clause)) # convert the clauses to CNF and add them to a list
        negationOfQuery = Clause(operator="~",right=query)
        cnfClausesList.append(convertToCNF(negationOfQuery))  # convert the negation of query to CNF and add to the list
        cnfClausesList = [str(clause).replace("(","").replace(")","") for clause in cnfClausesList] # remove all ()
        clauses = []
        for clause in cnfClausesList:
            for disjunctionOfSymbol in clause.split("&"): # split the clause at &
                clauses.append(disjunctionOfSymbol)

        clauses = [clause.split("||") for clause in clauses] # split the clause at ||
        clauses = {frozenset(clause) for clause in clauses} # By making clauses a set, we can remove the duplicate symbols
        new = set()
        while True:
            clauseList = [list(clause) for clause in clauses] # convert the set back to List to use List operations

            for i in range(len(clauseList)-1):
                for j in range(i+1,len(clauseList)):
                    resolvents = []
                    canBeResolved = False
                    for literal in clauseList[i]:
                        if literal[0] != "~" and (("~"+ literal) in clauseList[j]): # check if there is a negation of the symbol in clauseList[j]
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
                    if [] in resolvents: # return true if the list contain an empty list
                        return True

                    resolventsSet = {frozenset(clause) for clause in resolvents}
                    new = new.union(resolventsSet) # the union of new and resolventsSet

            if new.issubset(clauses): # return false if there is no new clause has been resolved
                return False
            clauses = clauses.union(new)# the union of clauses and new






if (__name__ == "__main__"):
    from generalLogicParser import parseClause
    from environment import Environment
    env = Environment()
    env.readFile("test.txt")
    resolution = Resolution()


    # resolution = Resolution()
    # clause1 = parseClause("a&b&c&d&e => f")
    # clause2 = parseClause("a")
    # clause3 = parseClause("b")
    # clause4 = parseClause("c")
    # clause5 = parseClause("d")
    # clause6 = parseClause("e")
    # query = parseClause("f")
    # print(resolution.solve(kb=[clause1,clause2,clause3,clause4,clause5,clause6],query=query))




