from propositionalSymbol import PropositionalSymbol
from clause import Clause


def parseClause(clauseString):
    operators = ["(", ")", "||", "&", "~", "=>", "<=>"]
    clauseString = clauseString.strip()
    if not [operator for operator in operators if operator in clauseString]:
        return Clause(right=PropositionalSymbol(clauseString.strip()))
    else:
        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, 1, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == ">" and clauseString[i - 1] == "=" and clauseString[i - 2] == "<":
                return Clause(left=parseClause(clauseString[:i-2]), right=parseClause(clauseString[i+1:]), operator="<=>")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, 0, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis +=1
            if openParenthesis == closeParenthesis and clauseString[i] == ">" and clauseString[i - 1] == "=":
                return Clause(left=parseClause(clauseString[:i-1]), right=parseClause(clauseString[i+1:]), operator="=>")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, 0, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == "|" and clauseString[i - 1] == "|":
                return Clause(left=parseClause(clauseString[:i-1]), right=parseClause(clauseString[i+1:]), operator="||")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, -1, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == "&":
                leftClause = parseClause(clauseString[:i])
                rightClause = parseClause(clauseString[i+1:])

                return Clause(left=leftClause, right=rightClause, operator="&")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, -1, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == "~":
                rightClause = parseClause(clauseString[i+1:])

                return Clause(right=rightClause, operator="~") # does not work with ~~a

        return parseClause(clauseString.strip().strip("()"))

if __name__ == "__main__":
    clause = parseClause("a || b")
    clause.setPropositionalSymbol([PropositionalSymbol('a',True),PropositionalSymbol('b',True)])
    print(clause.getValue())





