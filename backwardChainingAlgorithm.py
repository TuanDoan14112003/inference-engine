class BCAlgorithm:
    def __init__(self):
        self.foundSymbols = []

    def backwardChainingEntails(self, knowledgeBase, query):
        self.foundSymbols.append(query.right.symbol)
        for clause in knowledgeBase:
            if clause.operator is None and clause.left is None:
                if hasattr(clause.right, "symbol"):
                    if (clause == query):
                        return True
        for clause in knowledgeBase:
            if clause.operator == "=>":
                if hasattr(clause.right, "symbol"):
                    if (clause.right == query):
                        if self.backwardChainingEntails(knowledgeBase, clause.left):
                            return True
        self.foundSymbols.reverse()          
        return False


if __name__ == "__main__":
    from environment import Environment

    env = Environment()
    env.readFile("file.txt")

    tt = BCAlgorithm()
    print(tt.backwardChainingEntails(env.knowledgeBase, env.query))
    print(tt.foundSymbols)  # foundSymbols must be reset to [] when forwardChainingEntails is called the second time