import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from backwardChainingAlgorithm import BCAlgorithm
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser


class TestBC(unittest.TestCase):
    def testBCWithHornCases(self):
        print("*"*20 + "Testing BC With horn cases" + "*"*20)
        parent_folder = "UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range( 50):
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env = Environment()
            env.readFile(filename)
            BCC = BCAlgorithm()
            kb = []
            query = sympy_parser(str(env.query).replace(
                "=>", ">>").replace("||", "|"))
            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            self.assertEqual(BCC.backwardChainingEntails(
                env.knowledgeBase, env.symbols, env.query), entails(query, kb))


if __name__ == "__main__":
    unittest.main()
