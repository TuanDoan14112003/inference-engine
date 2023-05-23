import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from resolutionAlgorithm import Resolution
from testGenerator import TestGenerator
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser

class TestResolution(unittest.TestCase):


    def testResolutionWithHornCases(self):
        parent_folder = "UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            env = Environment()
            env.readFile(filename)
            resolution = Resolution()
            kb = []
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            print(entails(query, kb))

            self.assertEqual(resolution.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
    def testResolutionWithGeneralCases(self):
        parent_folder = "UnitTest/testcases/general/"
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
            print(entails(query, kb))

            self.assertEqual(resolution.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
