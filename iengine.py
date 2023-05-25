from TTAlgorithm import TruthTableAlgorithm
from forwardChainingAlgorithm import ForwardChaining
from backwardChainingAlgorithm import BCAlgorithm
from resolutionAlgorithm import Resolution
from dpllAlgorithm import DPLLAlgorithm
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
        print("YES:", algorithm.kbCount)
    else:
        print("NO")
elif method == "FC":
    algorithm = ForwardChaining()
    if algorithm.forwardChainingEntails(environment.knowledgeBase,environment.symbols,environment.query):
        print("YES: ", end ="")
        print(*(algorithm.foundSymbols),sep=", ")
    else:
        print("NO")
elif method == "BC":
    algorithm = BCAlgorithm()
    if algorithm.backwardChainingEntails(environment.knowledgeBase,environment.symbols,environment.query):
        print("YES: ", end ="")
        print(*(algorithm.outputSymbols),sep=", ")
    else:
        print("NO")
elif method == "RES":
    algorithm = Resolution()
    if algorithm.solve(environment.knowledgeBase,environment.query):
        print("YES")
    else:
        print("NO")
elif method == "DPLL":
    algorithm = DPLLAlgorithm()
    if algorithm.solve(environment.knowledgeBase,environment.query):
        print("YES")
    else:
        print("NO")
else:
    raise Exception("There is no such method, the available methods are TT, FC, BC, RES, and DPLL")

