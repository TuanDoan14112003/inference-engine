
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from forwardChainingAlgorithm import ForwardChaining
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser

class TestFC(unittest.TestCase):

    def testFCWithHornCases(self):
        print("*"*20 + "Testing FC With horn cases" + "*"*20)
        parent_folder = "UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            # reading each file in the folder
            filename= parent_folder + "test"  + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env = Environment()
            env.readFile(filename)
            forwardChaining = ForwardChaining()
            kb = []
            # convert query and clauses to sympy format
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||","|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            self.assertEqual(forwardChaining.forwardChainingEntails(env.knowledgeBase,env.symbols, env.query),entails(query,kb))

if __name__ == "__main__":
    unittest.main()
