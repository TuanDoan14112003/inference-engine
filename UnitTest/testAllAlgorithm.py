import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from UnitTest.testDPLL import  TestDPLL
from UnitTest.testResolution import TestResolution
from UnitTest.testTruthTable import TestTruthTable
from UnitTest.testFC import  TestFC
from UnitTest.testBC import  TestBC

def testAllAlgorithm(kb_type):
    suite = unittest.TestSuite()
    if kb_type == "horn":
        suite.addTest(TestDPLL("testDPLLWithHornCases"))
        # suite.addTest(TestResolution("testResolutionWithHornCases"))
        suite.addTest(TestTruthTable("testTruthTableWithHornCases"))
        suite.addTest(TestFC("testFCWithHornCases"))
        suite.addTest(TestBC("testBCWithHornCases"))
    elif kb_type == "general":
        suite.addTest(TestDPLL("testDPLLWithGeneralCases"))
        suite.addTest(TestResolution("testResolutionWithGeneralCases"))
        suite.addTest(TestTruthTable("testTruthTableWithGeneralCases"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    testAllAlgorithm("horn")