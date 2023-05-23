import random
import string
from os import listdir

class TestGenerator:
    def __init__(self):
        self.symbols = []
        self.clauses = []

   
    def generateHornCase(self, parent_folder):
        current_number_of_test = len(listdir(parent_folder))
        for i in range(50):
            self.symbols = list(string.ascii_letters[:5])
            clauses = []
            for j in range(7):
                hornClause = list(
                    set(random.choices(self.symbols, k=random.randint(1, 5))))
                tail = hornClause[:-1]
                if len(hornClause) >= 2:
                    head = hornClause[-1]
                    clauseString = "&".join(tail) + " =>" + head
                    clauses.append(clauseString)
            literal = list(
                set(random.choices(self.symbols, k=random.randint(1, 3))))
            clauses.extend(literal)
            query = random.choice(self.symbols)
            while query in literal:
                query = random.choice(self.symbols)
            with open(parent_folder+"horn" + str(current_number_of_test + i)+".txt", "w") as file:
                file.write("TELL\n")
                for clause in clauses:
                    file.write(clause)
                    file.write("; ")
                file.write("\n")
                file.write("ASK\n")
                file.write(query)

    def generateGeneralCase(self,  parent_folder, number, maxdepth=10):
        current_number_of_test = len(listdir(parent_folder))
        for j in range(number):

            with open(parent_folder+"general" + str(current_number_of_test + j)+".txt", "w") as file:
                file.write("TELL\n")
            self.clauses = []
            self.symbols = {symbol: 1 for symbol in list(
                string.ascii_lowercase[:7])}
            symbol = random.choice(list(self.symbols.keys()))
            for i in range(0, 6):
                clause = "("
                firstSymbol = random.choice(list(self.symbols.keys()))
                secondSymbol = random.choice(list(self.symbols.keys()))
                while self.symbols[firstSymbol] + self.symbols[secondSymbol] > maxdepth or firstSymbol == secondSymbol:
                    firstSymbol = random.choice(list(self.symbols.keys()))
                    secondSymbol = random.choice(list(self.symbols.keys()))
                depth = self.symbols[firstSymbol] + self.symbols[secondSymbol]

                if (random.randint(0, 1) == 0):
                    firstSymbol = "~"+firstSymbol

                if (random.randint(0, 1) == 0):
                    secondSymbol = "~"+secondSymbol
                clause += firstSymbol
                operator = random.randint(0, 2)
                if operator == 0:
                    clause += "&"
                elif operator == 1:
                    clause += "||"
                elif operator == 2:
                    clause += "=>"
                elif operator == 3:
                    clause += "<=>"
                clause += secondSymbol
                clause += ")"
                self.symbols.update({clause: depth})

                with open(parent_folder+"general" + str(current_number_of_test + j)+".txt", "a") as file:
                    file.write(clause)
                    file.write(";")
            with open(parent_folder+"general" + str(current_number_of_test + j)+".txt", "a") as file:
                file.write("\n")
                file.write("ASK\n")
                file.write(symbol)


    def generateGeneralLogic(self, filename, number, maxdepth=10):
        with open(filename, "w") as file:
            file.write("")
        self.clauses = []
        self.symbols = {symbol: 1 for symbol in list(
            string.ascii_lowercase[:7])}
        for i in range(0, number):
            clause = "("
            firstSymbol = random.choice(list(self.symbols.keys()))
            secondSymbol = random.choice(list(self.symbols.keys()))
            while self.symbols[firstSymbol] + self.symbols[secondSymbol] > maxdepth or firstSymbol == secondSymbol:
                firstSymbol = random.choice(list(self.symbols.keys()))
                secondSymbol = random.choice(list(self.symbols.keys()))
            depth = self.symbols[firstSymbol] + self.symbols[secondSymbol]

            if (random.randint(0, 1) == 0):
                firstSymbol = "~"+firstSymbol

            if (random.randint(0, 1) == 0):
                secondSymbol = "~"+secondSymbol
            clause += firstSymbol
            operator = random.randint(0, 2)
            if operator == 0:
                clause += "&"
            elif operator == 1:
                clause += "||"
            elif operator == 2:
                clause += "=>"
            elif operator == 3:
                clause += "<=>"
            clause += secondSymbol
            clause += ")"
            self.symbols.update({clause: depth})

            with open(filename, "a") as file:
                file.write(clause)
                file.write("\n")


if __name__ == "__main__":
    # test1 = testGenrator()
    # test1.generateHornCase()
    import sys
    test2 = TestGenerator()
    # test2.generateGeneralCase(
    #     "UnitTest/testcases/resolution/resolution", 50, 3)
    test2.generateGeneralCase("UnitTest/testcases/general/",50,3)
