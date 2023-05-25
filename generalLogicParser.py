from propositionalSymbol import PropositionalSymbol
from clause import Clause


def parseClause(clauseString):
    """This function will parse a clause string and returns a Clause object"""
    operators = ["(", ")", "||", "&", "~", "=>", "<=>"]
    clauseString = clauseString.strip() # remove any leading whitespace
    if not [operator for operator in operators if operator in clauseString]: # if the clause string does not contain any operators
        return Clause(right=PropositionalSymbol(clauseString.strip()))
    else:
        # check if the clause has <=>
        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, 1, -1): # going from right to left
            if clauseString[i] == "(":
                openParenthesis += 1 # count the open parenthesis
            elif clauseString[i] == ")":
                closeParenthesis += 1 # count the close parenthesis
            #check openParenthesis == closeParenthesis to make sure the current position is not in any inner parentheses
            if openParenthesis == closeParenthesis and clauseString[i] == ">" and clauseString[i - 1] == "=" and \
                    clauseString[i - 2] == "<":
                return Clause(left=parseClause(clauseString[:i - 2]), right=parseClause(clauseString[i + 1:]),
                              operator="<=>")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, 0, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == ">" and clauseString[i - 1] == "=":
                return Clause(left=parseClause(clauseString[:i - 1]), right=parseClause(clauseString[i + 1:]),
                              operator="=>")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, 0, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == "|" and clauseString[i - 1] == "|":
                return Clause(left=parseClause(clauseString[:i - 1]), right=parseClause(clauseString[i + 1:]),
                              operator="||")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, -1, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == "&":
                leftClause = parseClause(clauseString[:i])
                rightClause = parseClause(clauseString[i + 1:])

                return Clause(left=leftClause, right=rightClause, operator="&")

        openParenthesis = 0
        closeParenthesis = 0
        for i in range(len(clauseString) - 1, -1, -1):
            if clauseString[i] == "(":
                openParenthesis += 1
            elif clauseString[i] == ")":
                closeParenthesis += 1
            if openParenthesis == closeParenthesis and clauseString[i] == "~":
                rightClause = parseClause(clauseString[i + 1:])

                return Clause(right=rightClause, operator="~")  # double negation: ~(~a) not ~~a

        return parseClause(clauseString.strip()[1:-1])

def isCNF(clause):
    """This function will check if a clause is in CNF"""
    operators = ["=>", "<=>"]
    if [operator for operator in operators if operator in str(clause)]: # return false if clause has "=>" or "<=>"
        return False
    else:
        if clause.operator is None:
            return isinstance(clause.right,PropositionalSymbol) # check if the clause is a literal
        if clause.operator == "~":
            return isinstance(clause.right.right,PropositionalSymbol) # check if the clause is a literal
        if clause.operator == "||":
            return isDisjunctionOfLiterals(clause) # check if the clause is disjunction of literals
        if clause.operator == "&":
            return isCNF(clause.left) and isCNF(clause.right) # check if left and right clause is CNF
    return False

def isDisjunctionOfLiterals(clause):
    """This function will check if a clause is a disjunction of literals"""
    if clause.operator != "||":
        return False
    if isLiteral(clause.right) and isLiteral(clause.left) and clause.operator == "||":
        return True
    if isLiteral(clause.right) or isDisjunctionOfLiterals(clause.right):
        return isDisjunctionOfLiterals(clause.left) or isLiteral(clause.left)
    if isLiteral(clause.left) or isDisjunctionOfLiterals(clause.left):
        return isDisjunctionOfLiterals(clause.right) or isLiteral(clause.right)
    return False

def isLiteral(clause):
    """This function will check if the clause is a literal"""
    return isinstance(clause.right,PropositionalSymbol) or (clause.operator == "~" and isinstance(clause.right.right,PropositionalSymbol))


def convertToCNF(clause):
    """This function will convert the clause to CNF"""
    if isCNF(clause):
        return clause
    if clause.operator is None and clause.left is None and isinstance(clause.right, PropositionalSymbol): # make a new clause if the clause only has a single symbol
        return Clause(right=PropositionalSymbol(symbol=clause.right.symbol))
    elif clause.operator == "~" and isinstance(clause.right.right, PropositionalSymbol):
        return Clause(operator="~", right=Clause(right=PropositionalSymbol(clause.right.right.symbol)))

    # eliminate implication
    if clause.operator == "=>":
        return convertToCNF(Clause(left=Clause(right=clause.left, operator="~"), right=clause.right, operator="||"))
    elif clause.operator == "<=>":
        return convertToCNF(Clause(left=Clause(operator="||",
                                               left=Clause(
                                                   operator="~",
                                                   right=clause.left
                                               ),
                                               right=clause.right
                                               ), right=Clause(operator="||",
                                                               left=clause.left,
                                                               right=Clause(
                                                                   operator="~",
                                                                   right=clause.right)), operator="&"))

    # de morgan
    elif clause.operator == "~":
        if clause.right.operator == "~":
            return convertToCNF(clause.right.right)
        elif clause.right.operator == "&":
            return convertToCNF(Clause(left=Clause(operator="~", right=clause.right.left), right=Clause(operator="~", right=clause.right.right), operator="||"))
        elif clause.right.operator == "||":
            return convertToCNF(Clause(left=Clause(operator="~", right=clause.right.left), right=Clause(operator="~", right=clause.right.right), operator="&"))

    # distributive ( a || (b&c))
    elif clause.operator == "||" and clause.right.operator == "&":
        return convertToCNF(Clause(left=Clause(operator="||", left=clause.left, right=clause.right.left), right=Clause(operator="||", left=clause.left, right=clause.right.right), operator="&"))

    # distributive ( (b&c) || a)
    elif clause.operator == "||" and clause.left.operator == "&":
        return convertToCNF(Clause(left=Clause(operator="||", left=clause.right, right=clause.left.left), right=Clause(operator="||", left=clause.right, right=clause.left.right), operator="&"))

    final = Clause(right=convertToCNF(clause.right), left=convertToCNF(
        clause.left) if clause.left is not None else None, operator=clause.operator)
    if isCNF(final): # check if the final clause is in CNF
        return final
    else:
        return convertToCNF(final)



