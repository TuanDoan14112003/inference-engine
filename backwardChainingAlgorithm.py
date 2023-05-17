class BCAlgorithm:
    def __init__(self):
        self.frontier = []
        self.visited = []
        self.previous = []

    def backwardChainingEntails(self, knowledgeBase,symbols, query):
        if query.right.symbol not in symbols:
            return False
        inferred = {symbol: False for symbol in symbols}
        self.frontier = [query]
        self.foundSymbols = [clause.right.symbol for clause in knowledgeBase if
                             clause.operator is None and clause.left is None]
        self.visited = []
        while self.frontier:
            current = self.frontier.pop()
            if current.operator is None and current.left is None:
                if current.right.symbol not in self.visited:
                    self.visited.append(current.right.symbol)
                    for clause in knowledgeBase:
                        if clause.operator is None and clause.left is None:
                                if (clause.right == current.right):
                                    inferred[current.right.symbol] = True
                    # for clause in knowledgeBase:
                        if clause.operator == "=>":
                                if (clause.right == current):
                                    self.frontier.append(clause.left)
                                    self.previous.append({"left": clause.left, "right": current, "operator": "=>"})
            else:
                if (current.left.right.symbol in self.foundSymbols) and (current.right.right.symbol in self.foundSymbols):
                    inferred[current.right.right.symbol] = True
                    inferred[current.left.right.symbol] = True
                else:
                    if current.left.right.symbol not in self.visited:
                        self.frontier.append(current.left)
                    if current.right.right.symbol not in self.visited:
                        self.frontier.append(current.right)

      
        for i in self.previous.__reversed__():
            if i["left"].operator == None:
                if (inferred[i["left"].right.symbol] == True):
                    inferred[i["right"].right.symbol] = True 
            else:
                if (inferred[i["left"].right.right.symbol] == True) and (inferred[i["left"].left.right.symbol] == True):
                    inferred[i["right"].right.symbol] = True
        return inferred[query.right.symbol]



if __name__ == "__main__":
    from environment import Environment

    env = Environment()
    env.readFile("UnitTest/testcases/horns/horn0.txt")

    tt = BCAlgorithm()
    print(tt.backwardChainingEntails(env.knowledgeBase,env.symbols, env.query))
  