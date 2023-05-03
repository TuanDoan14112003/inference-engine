# craete truth table class

from propositionalSymbol import PropositionalSymbol
from clause import Clause


class TruthTable:
    def __init__(self):
        self.symbols = []
        self.clauses = []
        self.query = None

    # def addClause(self, clause):
    #     self.clauses.append(clause)
    #
    # def getClauses(self, i):
    #     return self.clauses[i]

    # def readFile(self, filename):
    #     with open(filename, 'r') as file:
    #         line = file.readline().strip()
    #         if line != "TELL":
    #             raise Exception("No TELL")
    #
    #         line = file.readline().strip()
    #         knowledgeBase = ""
    #         while line != "ASK":
    #             knowledgeBase += line
    #             line = file.readline().strip()
    #         self.query = file.readline().strip()
    #         clauses = knowledgeBase.split(";")
    #         clauses = [clause.strip() for clause in clauses if clause != ""]
    #         for clause in clauses:
    #             if "=>" in clause:
    #                 leftClause, rightClause = clause.split("=>")
    #                 leftSymbols = leftClause.split("&")
    #                 leftSymbols = [symbol.strip() for symbol in leftSymbols]
    #                 newClause = PropositionalSymbol(leftSymbols[0])
    #                 for i in range(1, len(leftSymbols)):
    #                     newClause = Clause(left=newClause, operator="&", right=PropositionalSymbol(leftSymbols[i]))
    #                 self.clauses.append(Clause(left=newClause,operator="=>",right=PropositionalSymbol(rightClause)))
    #
    #                 for symbol in leftSymbols:
    #                     if PropositionalSymbol(symbol) not in self.symbols:
    #                         self.symbols.append(PropositionalSymbol(symbol))
    #
    #                 if PropositionalSymbol(rightClause) not in self.symbols:
    #                     self.symbols.append(PropositionalSymbol(rightClause))
    #
    #             else:
    #                 if PropositionalSymbol(clause.strip()) not in self.symbols:
    #                     self.symbols.append(PropositionalSymbol(clause.strip()))
    #                     newClause = Clause(right=PropositionalSymbol(clause.strip()))
    #                     self.clauses.append(newClause)





if __name__ == "__main__":
    truthtable = TruthTable()
    truthtable.readFile("file.txt")

    for clause in truthtable.clauses:
        print(clause)
