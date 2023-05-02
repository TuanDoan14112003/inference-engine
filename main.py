import re
def readFile(filename):
    with open(filename,'r') as file:
        symbols = []
        operators = ["=>","&","~","||","<=>"]
        line = file.readline().strip()
        if line != "TELL":
            raise Exception("No TELL")

        line = file.readline().strip()
        knowledgeBase = ""
        while line != "ASK":
            knowledgeBase += line
            line = file.readline().strip()
        query = file.readline().strip()
        clauses = knowledgeBase.split(";")
        clauses = [clause.strip() for clause in clauses if clause != ""]
        for clause in clauses:
            if "=>" in clause:
                symbolList = re.split("=>|&" , clause)
                for symbol in symbolList:
                    if symbol.strip() not in symbols:
                        symbols.append(symbol.strip())
            else:
                if clause.strip() not in symbols:
                    symbols.append(clause.strip())

        print(symbols)






readFile("file.txt")