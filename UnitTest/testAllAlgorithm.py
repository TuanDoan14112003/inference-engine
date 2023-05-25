import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from UnitTest.testDPLL import  TestDPLL
from UnitTest.testResolution import TestResolution
from UnitTest.testTruthTable import TestTruthTable
from UnitTest.testFC import  TestFC
from UnitTest.testBC import  TestBC
import testGenerator


def testAllAlgorithm(kb_type):
    suite = unittest.TestSuite()
    test_generator = testGenerator.TestGenerator()
    if kb_type == "horn":
        test_generator.generateHornCase("UnitTest/testcases/horns/")
        suite.addTest(TestDPLL("testDPLLWithHornCases"))
        suite.addTest(TestResolution("testResolutionWithHornCases"))
        suite.addTest(TestTruthTable("testTruthTableWithHornCases"))
        suite.addTest(TestFC("testFCWithHornCases"))
        suite.addTest(TestBC("testBCWithHornCases"))
    elif kb_type == "general":
        test_generator.generateGeneralCase("UnitTest/testcases/general/",50,3)
        suite.addTest(TestDPLL("testDPLLWithGeneralCases"))
        suite.addTest(TestResolution("testResolutionWithGeneralCases"))
        suite.addTest(TestTruthTable("testTruthTableWithGeneralCases"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    testAllAlgorithm("general")
    testAllAlgorithm("horn")