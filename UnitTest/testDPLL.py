import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from dpllAlgorithm import DPLLAlgorithm
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser
from generalLogicParser import convertToCNF
class TestDPLL(unittest.TestCase):

    def testDPLLWithHornCases(self):
        print("*"*20 + "Testing DPLL With horn cases" + "*"*20)
        trueCount = 0
        parent_folder ="UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(0,50):
            filename= parent_folder + "test"  + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env = Environment()
            env.readFile(filename)
            dpll = DPLLAlgorithm()
            kb = []
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            rs = entails(query, kb)
            if rs:
                trueCount += 1

            self.assertEqual(dpll.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
    def testDPLLWithGeneralCases(self):
        print("*"*20 + "Testing DPLL With general cases" + "*"*20)
        trueCount = 0
        parent_folder ="UnitTest/testcases/general/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])

        for i in range(0,50):
            filename= parent_folder + "test"  + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env = Environment()
            env.readFile(filename)
            dpll = DPLLAlgorithm()
            kb = []
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
            rs = entails(query, kb)
            if rs:
                trueCount += 1

            self.assertEqual(dpll.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
