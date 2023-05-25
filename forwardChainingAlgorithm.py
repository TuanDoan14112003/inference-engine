class ForwardChaining:
    def __init__(self):
        self.foundSymbols = []
    def forwardChainingEntails(self, knowledgeBase, symbols, query):
        knowledgeBase = list({clause for clause in knowledgeBase}) # remove duplicate clauses
        self.foundSymbols = []
        count = {clause: clause.left.getNumberOfOperands() for clause in knowledgeBase if clause.operator == "=>"} # clause and their number of premises
        inferred = {symbol: False for symbol in symbols}
        agenda = [clause.right.symbol for clause in knowledgeBase if
                  clause.operator is None and clause.left is None]  # the list of symbol that is known to be true
        self.foundSymbols = agenda.copy()
        while agenda:
            if query.right.symbol in self.foundSymbols: # return true if the query is in self.foundSymbols
                return True
            symbol = agenda.pop()
            if not inferred[symbol]:
                inferred[symbol] = True
                for clause in knowledgeBase:
                    if clause.operator == "=>" and symbol in str(clause.left): # check if clause is in Horn form and symbol appears in clause.left
                        count[clause] -= str(clause.left).count(symbol)  #decrement count
                        if count[clause] == 0:
                            self.foundSymbols.append(clause.right.right.symbol)
                            if (clause.right == query):
                                return True #found the query
                            agenda.append(clause.right.right.symbol) #append symbol to agenda

        return False


if __name__ == "__main__":
    from environment import Environment

    env = Environment()
    env.readFile("file.txt")

    tt = ForwardChaining()
    print(tt.forwardChainingEntails(env.knowledgeBase, env.symbols, env.query))
    print(tt.foundSymbols)  # foundSymbols must be reset to [] when forwardChainingEntails is called the second time
