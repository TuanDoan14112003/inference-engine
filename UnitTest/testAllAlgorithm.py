import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from UnitTest.testDPLL import  TestDPLL
from UnitTest.testResolution import TestResolution
from UnitTest.testTruthTable import TestTruthTable
from UnitTest.testFC import  TestFC
from UnitTest.testBC import  TestBC
from testGenerator import TestGenerator

def testAllAlgorithm(kb_type):
    suite = unittest.TestSuite()
    testGenerator = TestGenerator()
    if kb_type == "horn":
        testGenerator.generateHornCase("UnitTest/testcases/Horn/")
        suite.addTest(TestDPLL("testDPLLWithHornCases"))
        suite.addTest(TestResolution("testResolutionWithHornCases"))
        suite.addTest(TestTruthTable("testTruthTableWithHornCases"))
        suite.addTest(TestFC("testFCWithHornCases"))
        suite.addTest(TestBC("testBCWithHornCases"))
    elif kb_type == "general":
        testGenerator.generateGeneralCase("UnitTest/testcases/general/",50, 4)
        suite.addTest(TestDPLL("testDPLLWithGeneralCases"))
        suite.addTest(TestResolution("testResolutionWithGeneralCases"))
        suite.addTest(TestTruthTable("testTruthTableWithGeneralCases"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    testAllAlgorithm("horn")