from propositionalSymbol import PropositionalSymbol
from copy import deepcopy


class TruthTableAlgorithm:
    def __init__(self):
        self.rowCount = 0
        self.kbCount = 0


    def validate(self, queryList, model):
        # query ist is a list of clauses [a&b&c => b]
        # model is a list of Propositional Symbol [a: True, b: False, c:True]
        for clause in queryList:
            clause.setPropositionalSymbol(model)
        for clause in queryList:
            if not clause.getValue():
                return False
        return True

    def checkAll(self, knowledgeBase, query, symbols, model):
        if not symbols:
            # for symbol in model:
            #     print(symbol.symbol + " " + str(symbol.value), end= "  ")
            # print()
            self.rowCount += 1
            if self.validate(knowledgeBase, model):
                self.kbCount += 1
                for symbol in model:
                    print(str(symbol.symbol) + ": " + str(symbol.value), end ="  ")
                print()
                return self.validate([query], model)
            else:
                return True
        else:
            symbol = symbols[0]
            oldSymbols = deepcopy(symbols)
            oldSymbols.pop(0)
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
        newModel = deepcopy(model)
        newPropositionalSymbol = PropositionalSymbol(symbol,value)
        newModel.append(newPropositionalSymbol)
        return newModel


if __name__ == "__main__":
    from environment import Environment
    import sympy
    env = Environment()
    env.readFile("UnitTest/testcases/horns/horn0.txt")
    print(env.query)
    tt = TruthTableAlgorithm()
    print(tt.checkAll(env.knowledgeBase,env.query,env.symbols,[]))
    print(tt.kbCount) # rowCount and kbCount must be reset to 0 when checkALl is called the second time with the same instance
    # print(tt.rowCount)