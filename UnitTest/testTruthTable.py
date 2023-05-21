import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from environment import Environment
from TTAlgorithm import TruthTableAlgorithm
import unittest
from testGenerator import TestGenerator
from sympy.logic.inference import entails
from sympy.parsing.sympy_parser import parse_expr as sympy_parser
from sympy import symbols
from sympy.logic.boolalg import truth_table
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestTruthTable(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        testGenerator = TestGenerator()
        testGenerator.generateGeneralCase(
            "UnitTest/testcases/general/general", 50, 10)

    def test_1(self):
        env = Environment()
        for i in range(50):
            env.readFile("UnitTest/testcases/general/general"+str(i)+".txt")
            truthTable = TruthTableAlgorithm()
            kb = []
            query = sympy_parser(str(env.query).replace(
                "=>", ">>").replace("||", "|"))
           

            
            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))
   
         
            print("Test1:",i)
            self.assertEqual(truthTable.checkAll(
                env.knowledgeBase, env.query, env.symbols, []), entails(query, kb))


if __name__ == "__main__":
    unittest.main()
