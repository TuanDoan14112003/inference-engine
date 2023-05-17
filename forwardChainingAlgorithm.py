class ForwardChaining:
    def __init__(self):
        self.foundSymbols = []

    def forwardChainingEntails(self, knowledgeBase, symbols, query):
        self.foundSymbols = []
        count = {clause: clause.left.getNumberOfOperands() for clause in knowledgeBase if clause.operator == "=>"}
        inferred = {symbol: False for symbol in symbols}
        agenda = [clause.right.symbol for clause in knowledgeBase if
                  clause.operator is None and clause.left is None]  # sai neu co ~
        self.foundSymbols = agenda.copy()
        while agenda:
            if query.right.symbol in self.foundSymbols: # !!!!!!!!!!!!!!!!!!!
                return True
            symbol = agenda.pop()
            if not inferred[symbol]:
                inferred[symbol] = True
                for clause in knowledgeBase:
                    if clause.operator == "=>" and symbol in str(clause.left):
                        count[clause] -= str(clause.left).count(symbol)
                        if count[clause] == 0:
                            self.foundSymbols.append(clause.right.right.symbol)
                            if (clause.right == query):
                                return True
                            agenda.append(clause.right.right.symbol)

        return False


if __name__ == "__main__":
    from environment import Environment

    env = Environment()
    env.readFile("UnitTest/testcases/horns/horn0.txt")

    tt = ForwardChaining()
    print(tt.forwardChainingEntails(env.knowledgeBase, env.symbols, env.query))
    print(tt.foundSymbols)  # foundSymbols must be reset to [] when forwardChainingEntails is called the second time
