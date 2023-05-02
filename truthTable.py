#craete truth table class
class TruthTable:
    def __init__(self):
        KB = []

    def addClause(self, clause):
        self.clauses.append(clause)

    def getClauses(self, i):
        return self.clauses[i]
    
    def query(self, query):
        for i in self.KB:
            if i == query:
                #query in KB
                print("true")
            else:
                continue
        return False
                
        