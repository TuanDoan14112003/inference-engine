from TTAlgorithm import TruthTableAlgorithm
from forwardChainingAlgorithm import ForwardChaining
from backwardChainingAlgorithm import BCAlgorithm
from environment import  Environment
import sys

if len(sys.argv) != 3:
    raise Exception("Wrong number of arguments")
method = sys.argv[1]
filename = sys.argv[2]
environment = Environment()
environment.readFile(filename)
if method == "TT":
    algorithm = TruthTableAlgorithm()
    if algorithm.checkAll(environment.knowledgeBase,environment.query,environment.symbols,[]):
        print("YES: ", algorithm.kbCount)
    else:
        print("NO")
elif method == "FC":
    algorithm = ForwardChaining()
    if algorithm.forwardChainingEntails(environment.knowledgeBase,environment.symbols,environment.query):
        print("YES: ", end ="")
        print(*algorithm.foundSymbols,sep=", ")
    else:
        print("NO")
elif method == "BC":
    pass
else:
    raise Exception("There is no such method, the available methods are TT, FC, and BC")

