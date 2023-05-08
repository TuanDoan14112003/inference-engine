import random
import string
class testGenrator:
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
        
        with open("horn.txt", "a") as file:
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
            

        with open("general.txt", "a") as file:
            file.write("TELL\n")
            for clause in self.clauses:
                file.write(clause)
                file.write("; ")
            file.write("\n")
            file.write("ASK\n")
            file.write(random.choice(string.ascii_lowercase))


if __name__ == "__main__":
    # test1 = testGenrator()
    # test1.generateHornCase()
    test2 = testGenrator()
    test2.generateGeneralCase()
