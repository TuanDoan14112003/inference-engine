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

    def testTruthTableWithHornCases(self):
        env = Environment()
        parent_folder ="UnitTest/testcases/horns/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env.readFile(filename)
            truthTable = TruthTableAlgorithm()
            kb = []
            query = sympy_parser(str(env.query).replace(
                "=>", ">>").replace("||", "|"))


            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))

            self.assertEqual(truthTable.checkAll(
                env.knowledgeBase, env.query, env.symbols, []), entails(query, kb))

    def testTruthTableWithGeneralCases(self):
        env = Environment()
        parent_folder = "UnitTest/testcases/general/"
        number_of_files = len([file for file in os.listdir(parent_folder) if "test" in file])
        for i in range(50):
            filename = parent_folder + "test" + str(number_of_files - 1 - i) + ".txt"
            print(filename)
            env.readFile(filename)
            truthTable = TruthTableAlgorithm()
            kb = []
            query = sympy_parser(str(env.query).replace(
                "=>", ">>").replace("||", "|"))

            for clause in env.knowledgeBase:
                kb.append(sympy_parser(str(clause).replace(
                    "=>", ">>").replace("||", "|")))

            self.assertEqual(truthTable.checkAll(
                env.knowledgeBase, env.query, env.symbols, []), entails(query, kb))


if __name__ == "__main__":
    unittest.main()
