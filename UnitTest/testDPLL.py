import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from dpllAlgorithm import DPLLAlgorithm
from testGenerator import TestGenerator
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser

class TestResolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testGenerator = TestGenerator()
        testGenerator.generateGeneralCase("testcases/resolution/resolution",50,3)

    def test(self):
        trueCount = 0
        for i in range(50):
            print(i)
            env = Environment()
            env.readFile("testcases/resolution/resolution" + str(i) + ".txt")
            dpll = DPLLAlgorithm()
            kb = []
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            rs = entails(query, kb)
            if rs:
                trueCount += 1
            print(rs)

            self.assertEqual(dpll.solve(env.knowledgeBase, env.query),
                             entails(query, kb))
        print((trueCount/50)*100,"%")
