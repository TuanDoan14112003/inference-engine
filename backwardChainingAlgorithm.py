from propositionalSymbol import PropositionalSymbol
from clause import Clause


class BCAlgorithm:
    def __init__(self):
        self.foundSymbols = []
        self.output = "NO"
        self.outputSymbols = []
        self.inferred = {}


    def backwardChainingEntails(self, kb, symbols, query):
        self.inferred = {symbol: False for symbol in symbols}
        self.foundSymbols = [clause.right.symbol for clause in kb if
                             clause.operator is None and clause.left is None]

        if self.infer(kb, query, []):
            self.output = "YES: "
            return True
        return False


    def infer(self, kb, query, explored):
       
        if (isinstance(query, Clause)):
            query = query.right

        if query.symbol in self.foundSymbols:
            if query.symbol not in self.foundSymbols:
                self.foundSymbols.append(query.symbol)
            return True
        
        for clause in kb:
            if (not isinstance(clause.right, PropositionalSymbol)):
                # Check if the right hand side of the sentence contain the symbol in the query
                if clause.right.right == query:
                    # Get all the symbols on the left hand side of the setence
                    leftHandSymbols = []
                    leftHandSymbols.append(clause.left.right)
                    premises = clause.left
                    while premises.left is not None:
                        premises = premises.left
                        leftHandSymbols.append(premises.right)
                    # Check if the left hand side symbols of the sentence is true in KB
                    trueSymbolCount = 0
                    for premise in leftHandSymbols:
                        
                        if (isinstance(premise, Clause)):
                            premise = premise.right
                        print(premise.symbol)
                        if premise == query:
                            break

                        if premise.symbol in explored:
                            if self.inferred[premise.symbol] == False:
                                break
                        else:
                            explored.append(premise.symbol)
                        
                        self.inferred[premise.symbol] = self.infer(
                            kb, premise, explored.copy())

                        if (self.inferred[premise.symbol] == False):
                            break
                        trueSymbolCount += 1
               

                    # Check if all the symbols in the left hand side is true
                    if trueSymbolCount == len(leftHandSymbols):
                        if query.symbol not in self.foundSymbols:
                            self.foundSymbols.append(query.symbol)
                        return True
        return False



if __name__ == "__main__":
    from environment import Environment

    env = Environment()
    env.readFile("file.txt")

    tt = BCAlgorithm()
    print(tt.backwardChainingEntails(env.knowledgeBase, env.symbols, env.query))
