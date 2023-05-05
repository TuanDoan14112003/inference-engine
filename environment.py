# create truth table class
import re

from propositionalSymbol import PropositionalSymbol
from clause import Clause
import generalLogicParser


class Environment:
    def __init__(self):
        self.symbols = []
        self.knowledgeBase = []
        self.query = None

    # def addClause(self, clause):
    #     self.knowledgeBase.append(clause)
    #
    # def getClauses(self, i):
    #     return self.knowledgeBase[i]

    def readFile(self, filename):
        with open(filename, 'r') as file:
            line = file.readline().strip()
            if line != "TELL":
                raise Exception("No TELL")

            line = file.readline().strip()
            knowledgeBase = ""
            while line != "ASK":
                knowledgeBase += line
                line = file.readline().strip()
            self.query = generalLogicParser.parseClause(file.readline().strip())
            clauses = knowledgeBase.split(";")
            clauses = [clause.strip() for clause in clauses if clause != ""]
            for clause in clauses:
                self.knowledgeBase.append(generalLogicParser.parseClause(clause))

            symbols = [symbol.strip() for symbol in re.split("~|&|\|\||=>|<=>|\(|\)|;", knowledgeBase) if
                       symbol.strip()]
            self.symbols = list(set(symbols))


if __name__ == "__main__":
    env = Environment()
    env.readFile("file.txt")

    print(env.symbols)
