from propositionalSymbol import PropositionalSymbol
from copy import deepcopy


class TruthTableAlgorithm:
    def __init__(self):
        self.rowCount = 0
        self.kbCount = 0


    def validate(self, queryList, model):
        # queryList is a list of clauses
        # model is a list of Propositional Symbol [a: True, b: False, c:True]
        for clause in queryList:
            clause.setPropositionalSymbol(model)
        for clause in queryList:
            if not clause.getValue():
                return False
        return True

    def checkAll(self, knowledgeBase, query, symbols, model):
        if not symbols:
            self.rowCount += 1
            if self.validate(knowledgeBase, model): # check if model of knowledge base
                self.kbCount += 1
                return self.validate([query], model) # check if model of query
            else:
                return True
        else:
            symbol = symbols[0]
            oldSymbols = deepcopy(symbols)
            oldSymbols.pop(0) # the rest of symbols
            return self.checkAll(knowledgeBase, query, oldSymbols, self.extend(symbol, True, model)) and self.checkAll(
                knowledgeBase, query, oldSymbols, self.extend(symbol, False, model))


    def generateTable(self,symbols, model):
        if not symbols:
            for symbol in model:
                print(symbol.symbol + "=" + str(symbol.value), end="  ")
            print()
            self.rowCount += 1
        else:
            symbol = symbols[0]
            oldSymbols = deepcopy(symbols)
            oldSymbols.pop(0)
            self.generateTable(oldSymbols,self.extend(symbol,True,model))
            self.generateTable(oldSymbols,self.extend(symbol,False,model))


    def extend(self, symbol, value, model):
        """This function extends the model with a new symbol"""
        newModel = deepcopy(model)
        newPropositionalSymbol = PropositionalSymbol(symbol,value)
        newModel.append(newPropositionalSymbol)
        return newModel


if __name__ == "__main__":
    """Testing"""
    from environment import Environment
    env = Environment()
    env.readFile("file.txt")
    tt = TruthTableAlgorithm()
    print(tt.checkAll(env.knowledgeBase,env.query,env.symbols,[]))
