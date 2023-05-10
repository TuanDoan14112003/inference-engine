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

                return Clause(right=rightClause, operator="~")  # does not work with ~~a

        return parseClause(clauseString.strip()[1:-1])

def isCNF(clause):
    operators = ["=>", "<=>"]
    if [operator for operator in operators if operator in str(clause)]:
        return False
    else:
        if clause.operator is None:
            return isinstance(clause.right,PropositionalSymbol)
        if clause.operator == "~":
            return isinstance(clause.right.right,PropositionalSymbol)
        if clause.operator == "||":

            # if isinstance(clause.left.right,PropositionalSymbol) or (clause.left.operator == "~" and isinstance(clause.left.right.right,PropositionalSymbol)):
            #     if isinstance(clause.right.right,PropositionalSymbol) or (clause.right.operator == "~" and isinstance(clause.right.right.right,PropositionalSymbol)):
            #         return True
            #
            # if not isinstance(clause.left.right,PropositionalSymbol):
            #     if clause.left.operator != "||":
            #         return False
            # if not isinstance(clause.right.right,PropositionalSymbol):
            #     if clause.right.operator != "||":
            #         return False
            #
            # if not isinstance(clause.left.right,PropositionalSymbol) or not isinstance(clause.right.right,PropositionalSymbol):
            #     return isCNF(clause.left) and isCNF(clause.right)
            # return False
            return isDisjunctionOfLiterals(clause)



        if clause.operator == "&":
            return isCNF(clause.left) and isCNF(clause.right)

    return False

def isDisjunctionOfLiterals(clause):
    if clause.operator != "||":
        return False
    if isLiteral(clause.right) and isLiteral(clause.left) and clause.operator == "||":
        return True
    if isLiteral(clause.right) or isDisjunctionOfLiterals(clause.right):
        return isDisjunctionOfLiterals(clause.left)
    if isLiteral(clause.left) or isDisjunctionOfLiterals(clause.left):
        return isDisjunctionOfLiterals(clause.right)
    return False

def isLiteral(clause):
    return isinstance(clause.right,PropositionalSymbol) or (clause.operator == "~" and isinstance(clause.right.right,PropositionalSymbol))



def convertToCNF(clause):
    if clause.operator is None and clause.left is None and isinstance(clause.right,PropositionalSymbol):
        return Clause(right=PropositionalSymbol(symbol=clause.right.symbol))
    elif clause.operator == "~" and isinstance(clause.right.right,PropositionalSymbol):
        return Clause(operator="~",right=Clause(right=PropositionalSymbol(clause.right.right.symbol)))



    # eliminate implication
    if clause.operator == "=>":
        newLeft = convertToCNF(Clause(right=convertToCNF(clause.left), operator="~"))
        newRight = convertToCNF(clause.right)
        return convertToCNF(Clause(left=newLeft, right=newRight, operator="||"))
    elif clause.operator == "<=>":
        newLeft = convertToCNF(Clause(operator="||",
                         left=Clause(
                             operator="~",
                             right=convertToCNF(clause.left)
                         ),
                         right=convertToCNF(clause.right)
                         ))

        newRight = convertToCNF(Clause(operator="||",
                          left=convertToCNF(clause.left),
                          right=Clause(
                              operator="~",
                              right=convertToCNF(clause.right))))

        return convertToCNF(Clause(left=newLeft, right=newRight, operator="&"))

    #de morgan
    elif clause.operator == "~":
        if clause.right.operator == "~":
            return convertToCNF(clause.right.right)
        elif clause.right.operator == "&":
            newLeft = convertToCNF(Clause( operator="~",right=convertToCNF(clause.right.left)))
            newRight = convertToCNF(Clause( operator="~",right=convertToCNF(clause.right.right)))
            return convertToCNF(Clause(left=newLeft, right=newRight, operator="||"))
        elif clause.right.operator == "||":
            newLeft = convertToCNF(Clause( operator="~",right=convertToCNF(clause.right.left)))
            newRight = convertToCNF(Clause(operator="~", right=convertToCNF(clause.right.right)))
            return convertToCNF(Clause(left=newLeft, right=newRight, operator="&"))

    #distributive ( a || (b&c))
    elif clause.operator == "||" and clause.right.operator == "&":
        newLeft = convertToCNF(Clause(operator = "||", left= convertToCNF(clause.left),right = convertToCNF(clause.right.left)))
        newRight = convertToCNF(Clause(operator = "||",left = convertToCNF(clause.left),right = convertToCNF(clause.right.right)))
        return convertToCNF(Clause(left=newLeft,right=newRight,operator="&"))

    #distributive ( (b&c) || a)
    elif clause.operator == "||" and clause.left.operator == "&":
        newLeft = convertToCNF(Clause(operator = "||", left= convertToCNF(clause.right),right = convertToCNF(clause.left.left)))
        newRight = convertToCNF(Clause(operator = "||",left = convertToCNF(clause.right),right = convertToCNF(clause.left.right)))
        return convertToCNF(Clause(left=newLeft,right=newRight,operator="&"))

    final = Clause(right=convertToCNF(clause.right),left=convertToCNF(clause.left) if clause.left is not None else None,operator=clause.operator)
    print(final)
    if isCNF(final):
        return final
    else:
        return convertToCNF(final)
    # return final


if __name__ == "__main__":
    # oldClause = parseClause("~a||b")
    # clause.setPropositionalSymbol([PropositionalSymbol('a',True),PropositionalSymbol('b',True)])
    # print(oldClause)

    import sympy

    # from sympy.logic.boolalg import is_cnf
    # print(is_cnf("a & ~b"))
    # # test cnf
    # clause = parseClause("~(a=>b)")

    # clause = parseClause("(a || b || c || d || ~e) & (c || ~d) & a & c")
    # # print(isCNF(clause))

    # clause = parseClause("(~(~(~d&f)||~(~(~b&~f)&~a))||~(~b&~f))")
    # newClause = convertToCNF(clause)
    print(isCNF(parseClause("((b||f)||((~a)||(~a)))")))
    # print(newClause)
    # print(isCNF(parseClause("~a||~b||~c")))
    #
    import sympy
    print(sympy.to_cnf("(~(~(~d&f)|~(~(~b&~f)&~a))|~(~b&~f))"))
    # clause2 = parseClause("~(a=>b)")
    # print(newClause == clause2)
    # print(sympy.simplify("(((d|((~c)|(~c)))&(d|((~c)|(~a))))&((d|(b|(~c)))&(d|(b|(~a)))))"))
    # print(sympy.simplify("(d | ~c) & (b | d | ~a)"))

    # print(isDisjunctionOfLiterals(parseClause("a & a")))
