import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import generalLogicParser as parser
import unittest
from testGenerator import TestGenerator
import sympy
from sympy.logic.boolalg import  is_cnf
from sympy.parsing.sympy_parser import parse_expr as sympy_parser
#generate a simple unit test

class TestCNF(unittest.TestCase):
    number_of_files = len(os.listdir("UnitTest/testcases/cnf/"))
    filename = "UnitTest/testcases/cnf/" + "cnf" + str(number_of_files) + ".txt"
    @classmethod
    def setUpClass(cls):
        testGenerator = TestGenerator()
        testGenerator.generateGeneralLogic(cls.filename, 100,5)
        print(cls.filename)
        
    def testGeneralLogicParser(self):
        with open(self.__class__.filename, "r") as file:
            line = file.readline().strip()
            while line:
                exp1 = sympy_parser(line.replace("=>", ">>").replace("||","|"))
                exp2 = sympy_parser(str(parser.parseClause(line)).replace("=>", ">>").replace("||", "|"))
                print(parser.parseClause(line))
                print("vs")
                print(exp2)
                print("*"*20)
                self.assertTrue(exp1.equals(exp2))
                line = file.readline().strip()
                
    def testCNF(self):

        with open(self.__class__.filename, "r") as file:
            line = file.readline().strip()
            count = 1
            while line:
                exp1 = parser.convertToCNF(parser.parseClause(line))
                exp2 = sympy.to_cnf(line.replace(
                    "=>", ">>").replace("||", "|"))
                print(line)
                # print(exp1)
                # print("vs")
                # print(exp2)
                # print("*"*20)


                self.assertTrue(is_cnf(str(exp1).replace(
                    "=>", ">>").replace("||", "|")))
                self.assertTrue(exp2.equals(sympy_parser(str(exp1).replace("=>", ">>").replace("||","|"))))
                line = file.readline().strip()
                count += 1

if __name__ == '__main__':
    unittest.main()



