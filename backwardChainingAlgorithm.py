from propositionalSymbol import PropositionalSymbol
from clause import Clause


class BCAlgorithm:
    def __init__(self):
        self.frontier = []
        self.visited = []
        self.previous = []
        self.foundSymbols = []

    # def backwardChainingEntails(self, knowledgeBase,symbols, query):
    #     if query.right.symbol not in symbols:
    #         return False
    #     inferred = {symbol: False for symbol in symbols}
    #     self.frontier = [query]
    #     self.foundSymbols = [clause.right.symbol for clause in knowledgeBase if
    #                          clause.operator is None and clause.left is None]
        

    #     while self.frontier:
    #         current = self.frontier.pop(0)
            
    #         if (isinstance(current, Clause)):
    #             current = current.right
    #         print("Current: ", current.symbol)
    #         if current.symbol not in self.visited:
    #             for clause in knowledgeBase:
    #                 if isinstance(clause.right, Clause):
    #                     rightclause = clause.right
    #                 if rightclause.right.symbol == current.symbol:
    #                     if clause.operator is None and clause.left is None:
    #                         inferred[clause.right.symbol] = True
    #                     elif clause.operator == "=>":
    #                         if clause.left.right.symbol in self.foundSymbols and (clause.left.left is None or clause.left.getNumberOfOperands() == 1  or clause.left.left.symbol in self.foundSymbols):
    #                             if (isinstance(clause.right, Clause)):
    #                                 self.foundSymbols.append(clause.right.right.symbol)
    #                                 inferred[clause.right.right.symbol] = True
    #                             else:
    #                                 self.foundSymbols.append(clause.right.symbol)
    #                                 inferred[clause.right.symbol] = True
    #                             self.previous.append({"conclusion": clause.right, "premises": [clause.left.right]})
    #                             if clause.left.left is not None:
    #                                 self.previous[-1]["premises"].append(clause.left.left)
    #                         else:
    #                             self.frontier.append(clause.left.right)
    #                             while clause.left.left is not None:
    #                                 clause = clause.left
    #                                 self.frontier.append(clause.right)
                                
                         
    #     self.previous.reverse()
    #     for clause in self.previous:
    #         print("Conclusion: ", clause["conclusion"])
    #         results = []
    #         for premise in clause["premises"]:
    #             print("Premise: ", premise)
    #             results.append(inferred[premise.symbol])
    #         if all(results):
    #             inferred[clause["conclusion"].right.symbol] = True

                
    #     return inferred[query.right.symbol]

            
    def backwardChainingEntails(self, knowledgeBase, symbols, query):
        if self.foundSymbols == []:
            self.foundSymbols = [clause.right.symbol for clause in knowledgeBase if
                                 clause.operator is None and clause.left is None]

        # Check if the query is a Clause
        if (isinstance(query, Clause)):
            query = query.right
        if query.symbol in self.visited:
            return False
        self.visited.append(query.symbol)
        if query.symbol not in symbols:
            return False
        # Check if the query is a fact
        if query.symbol in self.foundSymbols:
            self.visited.remove(query.symbol)
            return True
    # Iterate through each rule in the knowledge base
        for rule in knowledgeBase:
            # Check if the conclusion of the rule matches the goal
            if (not isinstance(rule.right, PropositionalSymbol)):
                if rule.right.right == query and rule not in self.visited:
                    # Recursively evaluate the premises of the rule
                    premises = rule.left
                    result = []
                    result.append(self.backwardChainingEntails(
                        knowledgeBase, symbols, premises.right))

                    # If the rule has more than one premise, evaluate the rest of the premises
                    while premises.left is not None:
                        premises = premises.left
                        result.append(self.backwardChainingEntails(
                            knowledgeBase, symbols, premises.right))
                    # If all premises are true, return True
                    if all(result):
                        self.visited.remove(query.symbol)
                        return True

        # If no rule matches the goal, return False

        return False



if __name__ == "__main__":
    from environment import Environment

    env = Environment()
    env.readFile("horn.txt")

    tt = BCAlgorithm()
    print(tt.backwardChainingEntails(env.knowledgeBase, env.symbols, env.query))

