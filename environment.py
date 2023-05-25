import re
import generalLogicParser


class Environment:
    """This class represents the environment which includes the knowledge base and the query"""
    def __init__(self):
        self.symbols = [] # the list of symbols in the knowledge base
        self.knowledgeBase = []
        self.query = None


    def readFile(self, filename):
        """This function will read a file and create an Environment object"""
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
            clauses = [clause.strip() for clause in clauses if clause.strip() != ""] # remove empty clause
            for clause in clauses:
                self.knowledgeBase.append(generalLogicParser.parseClause(clause)) # parse the clause string

            symbols = [symbol.strip() for symbol in re.split("~|&|\|\||=>|<=>|\(|\)|;", knowledgeBase) if
                       symbol.strip()] # using regex to get all the symbols in the knowledgebase
            self.symbols = list(set(symbols)) # remove duplicates


if __name__ == "__main__":
    env = Environment()
    env.readFile("file.txt")

    print(env.symbols)
