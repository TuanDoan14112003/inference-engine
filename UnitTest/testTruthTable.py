import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from environment import Environment
from TTAlgorithm import TruthTableAlgorithm
import unittest
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser
from generalLogicParser import convertToCNF

class TestTruthTable(unittest.TestCase):

    #test for TT algorithm with horn cases
    def testTruthTableWithHornCases(self):
        print("*"*20 + "Testing TT With horn cases" + "*"*20)
        parent_folder = "UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            env = Environment()

            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env.readFile(filename)
            truthTable = TruthTableAlgorithm()
            kb = []
            # convert query and clauses to sympy format
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))


            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            self.assertEqual(truthTable.checkAll(
                env.knowledgeBase, env.query, env.symbols, []), entails(query, kb))

    #test for TT algorithm with general cases
    def testTruthTableWithGeneralCases(self):
        print("*"*20 + "Testing TT With general cases" + "*"*20)

        parent_folder = "UnitTest/testcases/general/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            env = Environment()
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env.readFile(filename)
            truthTable = TruthTableAlgorithm()
            kb = []
            # convert query and clauses toCNF
            # Then convert query and clauses to sympy format
            if "<=>" in str(env.query):
                query = sympy_parser(str(convertToCNF(env.query)).replace("=>", ">>").replace("||", "|"))
            else:
                query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                if "<=>" in str(clause):
                    kb.append(sympy_parser(str(convertToCNF(clause)).replace(
                        "=>", ">>").replace("||", "|")))
                else:
                    kb.append(sympy_parser(str(clause).replace(
                        "=>", ">>").replace("||", "|")))
            self.assertEqual(truthTable.checkAll(
                env.knowledgeBase, env.query, env.symbols, []), entails(query, kb))


if __name__ == "__main__":
    unittest.main()
