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
            file.close()

    def generateGeneralCase(self):
        pass


if __name__ == "__main__":
    test = testGenrator()
    test.generateHornCase()
