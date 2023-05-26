import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from resolutionAlgorithm import Resolution
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser
from generalLogicParser import convertToCNF
class TestResolution(unittest.TestCase):
    def testResolutionWithHornCases(self):
        print("*"*20 + "Testing Resolution With horn cases" + "*"*20)
        parent_folder = "UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env = Environment()
            env.readFile(filename)
            resolution = Resolution()
            kb = []
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            self.assertEqual(resolution.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
    def testResolutionWithGeneralCases(self):
        print("*"*20 + "Testing Resolution With general cases" + "*"*20)
        parent_folder = "UnitTest/testcases/general/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            # reading each file in the folder
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env = Environment()
            env.readFile(filename)
            resolution = Resolution()
            kb = []
            # convert query and clauses toCNF
            # Then convert query and clauses to sympy format
            if "<=>" in str(env.query):
                query = sympy_parser(str(convertToCNF(env.query)).replace("=>", ">>").replace("||", "|")) # As sympy does not have <=> symbol, we have to convert the clause to CNF
            else:
                query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                if "<=>" in str(clause):
                    kb.append(sympy_parser(str(convertToCNF(clause)).replace(
                        "=>", ">>").replace("||", "|")))
                else:
                    kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))

            self.assertEqual(resolution.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
