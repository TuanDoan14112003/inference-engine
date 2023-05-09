import random
import string
class TestGenrator:
    def __init__(self):
        self.symbols = []
        self.clauses = []

    def generateHornCase(self):
        for i in range(1, 10):
            clause = ""
            if (random.randint(0, 1) == 0):
                for j in range(1, 2):
                    clause += random.choice(string.ascii_lowercase)
                    clause += "&"
                clause += random.choice(string.ascii_lowercase)
                clause += " => "
                clause += random.choice(string.ascii_lowercase)
            else:
                clause += random.choice(string.ascii_lowercase)
            self.clauses.append(clause)
        
        with open("horn.txt", "w") as file:
            file.write("TELL\n")
            for clause in self.clauses:    
                file.write(clause)
                file.write("; ")
            file.write("\n")
            file.write("ASK\n")
            file.write(random.choice(string.ascii_lowercase))

    def generateGeneralCase(self):
        for i in range(1, 10):
            clause = ""
            if (random.randint(0, 1) == 0):
                for j in range(1, 2):
                    clause += random.choice(string.ascii_lowercase)
                    operator = random.randint(0, 3)
                    if operator == 0:
                        clause += "&"
                    elif operator == 1:
                        clause += "||"
                    elif operator == 2:
                        clause += "=>"
                    elif operator == 3:
                        clause += "<=>"
                clause += random.choice(string.ascii_lowercase)
                operator = random.randint(0, 3)
                if operator == 0:
                    clause += "&"
                elif operator == 1:
                    clause += "||"
                elif operator == 2:
                    clause += "=>"
                elif operator == 3:
                    clause += "<=>"
                clause += random.choice(string.ascii_lowercase)
            else:
                clause += random.choice(string.ascii_lowercase)
            
            if (len(clause) > 1):
                if (random.randint(0, 1) == 0):
                    if (clause[-4] == "=" or clause[-4] == "|") and clause[-5] != "<":
                        clause += ")"
                        clause = clause[:-5]+"("+clause[-5:]
                    elif clause[-4] == "=" and clause[-5] != "<":
                        clause += ")"
                        clause = clause[:-6]+"("+clause[-6:]
            self.clauses.append(clause)

        with open("general.txt", "w") as file:
            file.write("TELL\n")
            for clause in self.clauses:
                file.write(clause)
                file.write("; ")
            file.write("\n")
            file.write("ASK\n")
            file.write(random.choice(string.ascii_lowercase))

    def generateGeneralLogic(self,filename, number):
        with open(filename, "w") as file:
            file.write("")
        self.clauses = []
        self.symbols = []
        self.symbols = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        for i in range(0, number):
            clause = "("
            firstSymbol = random.choice(self.symbols)
            secondSymbol = random.choice(self.symbols)
            while (firstSymbol == secondSymbol):
                secondSymbol = random.choice(self.symbols)
                
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
            self.symbols.append(clause)
            with open(filename, "a") as file:
                    file.write(clause)
                    file.write("\n")



        
        
       


if __name__ == "__main__":
    # test1 = testGenrator()
    # test1.generateHornCase()
    import sys
    test2 =TestGenrator()
    test2.generateGeneralLogic(sys.argv[1])
