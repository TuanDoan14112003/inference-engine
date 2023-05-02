from propositionalSymbol import PropositionalSymbol
from copy import deepcopy
class TTAlgorithm:
    def __init__(self):
        self.query = None

    def validate(self, queryList, model):
        #query ist is a list of clauses [a&b&c => b]
        #model is a list of Propositional Symbol [a: True, b: False, c:True]

    def checkAll(self,knowledgeBase, query, symbols, model):
        if not symbols:

        else:
            symbol = symbols.pop()
            oldSymbols = symbols.deepcopy()
            return self.checkAll(knowledgeBase,query,oldSymbols,self.extend(symbol,True,model)) and self.checkAll(knowledgeBase,query,oldSymbols,self.extend(symbol,False,model))

    def extend(self,symbol,value,model):
        newModel = model.deepcopy()
        newPropositionalSymbol = PropositionalSymbol(symbol)
        newPropositionalSymbol.setValue(value)
        newModel.append(newPropositionalSymbol)
        return newModel


