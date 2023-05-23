
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from forwardChainingAlgorithm import ForwardChaining
from backwardChainingAlgorithm import BCAlgorithm
from testGenerator import TestGenerator
from environment import Environment
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser

class TestFCBC(unittest.TestCase):

    def test_1(self):
    
        for i in range(50):
            env = Environment()
            env.readFile("UnitTest/testcases/horns/horn"+str(i)+".txt")
            forwardChaining = ForwardChaining()
            backwardChaining = BCAlgorithm()
            FCresult = forwardChaining.forwardChainingEntails(
                env.knowledgeBase, env.symbols, env.query)
            BCresult = backwardChaining.backwardChainingEntails(
                env.knowledgeBase, env.symbols, env.query)
            print("Test1:",i)
            print("FC: ",FCresult )
            print("BC: ", BCresult)
            print("*"*20)
            self.assertEqual(FCresult,BCresult)

    def test_2(self):
        for i in range(50):
            print("Test2:",i)
            env = Environment()
            env.readFile("UnitTest/testcases/horns/horn"+str(i)+".txt")
            forwardChaining = ForwardChaining()
            kb = []
            query = sympy_parser(str(env.query).replace("=>", ">>").replace("||","|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
            print(entails(query, kb))
            self.assertEqual(forwardChaining.forwardChainingEntails(env.knowledgeBase,env.symbols, env.query),entails(query,kb))

    def test_3(self):
        for i in range( 50):
            print("Test3:",i)
            env = Environment()
            env.readFile("UnitTest/testcases/horns/horn"+str(i)+".txt")
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
