from propositionalSymbol import PropositionalSymbol
from clause import Clause


class BCAlgorithm:
    def __init__(self):
        self.frontier = []
        self.visited = []
        self.previous = []

    # def backwardChainingEntails(self, knowledgeBase,symbols, query):
    #     if query.right.symbol not in symbols:
    #         return False
    #     inferred = {symbol: False for symbol in symbols}
    #     self.frontier = [query]
    #     self.foundSymbols = [clause.right.symbol for clause in knowledgeBase if
    #                          clause.operator is None and clause.left is None]
    #     self.visited = []
    #     while self.frontier:
    #         current = self.frontier.pop()
    #         if current.operator is None and current.left is None:
    #             if current.right.symbol not in self.visited:
    #                 self.visited.append(current.right.symbol)
    #                 for clause in knowledgeBase:
    #                     if clause.operator is None and clause.left is None:
    #                             if (clause.right == current.right):
    #                                 inferred[current.right.symbol] = True
    #                # for clause in knowledgeBase:
    #                     if clause.operator == "=>":
    #                             if (clause.right == current):
    #                                 self.frontier.append(clause.left)
    #                                 self.previous.append({"left": clause.left, "right": current, "operator": "=>"})
    #         else:
    #             if (isinstance(current.left.right,PropositionalSymbol)):
    #                 if (current.left.right.symbol in self.foundSymbols) and (current.right.right.symbol in self.foundSymbols):
    #                     inferred[current.right.right.symbol] = True
    #                     inferred[current.left.right.symbol] = True
    #                 else:
    #                     if current.left.right.symbol not in self.visited:
    #                         self.frontier.append(current.left)
    #                     if current.right.right.symbol not in self.visited:
    #                         self.frontier.append(current.right)
    #             else:
    #                 if (current.right.right.symbol in self.foundSymbols):
    #                     inferred[current.right.right.symbol] = True
    #                 else:
    #                     self.frontier.append(current.right)

    #                 self.frontier.append(current.left)

    #     for i in self.previous.__reversed__():
    #         if i["left"].operator == None:
    #             if (inferred[i["left"].right.symbol] == True):
    #                 inferred[i["right"].right.symbol] = True
    #         else:
    #             if (isinstance(i["left"].left.right, PropositionalSymbol)):
    #                 if (inferred[i["left"].right.right.symbol] == True) and (inferred[i["left"].left.right.symbol] == True):
    #                     inferred[i["right"].right.symbol] = True
    #             else:
    #                 list = []
    #                 current = i["left"].left
    #                 while (current != None):
    #                     list.append(i["left"].right.right.symbol)
    #                     current = current.left
    #                 for j in list:
    #                     if inferred[j] == False:
    #                         inferred[i["right"].right.symbol] = False
    #                 inferred[i["right"].right.symbol] = True
    #     return inferred[query.right.symbol]

    def backwardChainingEntails(self, knowledgeBase, symbols, query):
      
    
        # Check if the query is a Clause
        if (isinstance(query, Clause)):
            query = query.right
        if query.symbol in self.visited:
            return False
        self.visited.append(query.symbol)
    # Iterate through each rule in the knowledge base
        for rule in knowledgeBase:
            # Check if the conclusion of the rule matches the goal
            if (isinstance(rule.right, PropositionalSymbol)):
                if rule.right == query:
                    # Recursively evaluate the premises of the rule
                    self.visited.remove(query.symbol)
                    return True
            else:
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
    env.readFile("UnitTest/testcases/horns/horn13.txt")

    tt = BCAlgorithm()
    print(tt.backwardChainingEntails(env.knowledgeBase, env.symbols, env.query))
