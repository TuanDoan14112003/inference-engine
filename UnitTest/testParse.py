import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import generalLogicParser as parser
import unittest
from testGenerator import TestGenrator
import sympy
#generate a simple unit test

class TestCNF(unittest.TestCase):
    def testGeneralLogicParser(self):
        testGenerator = TestGenrator()
        testGenerator.generateGeneralLogic("testcases/general.txt",5000)
        with open("testcases/general.txt", "r") as file:
            line = file.readline().strip()
            while line:
                
                exp1 = sympy.parsing.sympy_parser.parse_expr(
                    line.replace("=>", ">>").replace("||","|"))
                exp2 = sympy.parsing.sympy_parser.parse_expr(
                    str(parser.parseClause(line)).replace("=>", ">>").replace("||", "|"))
                print(parser.parseClause(line))
                print("vs")
                print(sympy.parsing.sympy_parser.parse_expr(line.replace("=>", ">>").replace("||", "|")))
                print("*"*20)
                self.assertTrue(exp1.equals(exp2))
                line = file.readline().strip()
    def testCNF(self):
        testGenerator = TestGenrator()
        testGenerator.generateCNF("testcases/cnf.txt", 5000)
        with open("testcases/cnf.txt", "r") as file:
            line = file.readline().strip()
            while line:
                exp1 = sympy.parsing.sympy_parser.parse_expr(
                    line.replace("=>", ">>").replace("||", "|"))
                exp2 = sympy.parsing.sympy_parser.parse_expr(
                    str(parser.parseClause(line)).replace("=>", ">>").replace("||", "|"))
                print(parser.parseClause(line))
                print("vs")
                print(sympy.parsing.sympy_parser.parse_expr(line.replace("=>", ">>").replace("||", "|")))
                print("*"*20)
                self.assertTrue(exp1.equals(exp2))
                line = file.readline().strip()

if __name__ == '__main__':
    unittest.main()



