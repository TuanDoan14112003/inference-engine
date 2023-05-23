import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from UnitTest.testDPLL import  TestDPLL
from UnitTest.testResolution import TestResolution
from UnitTest.testTruthTable import TestTruthTable


if __name__ == '__main__':
    test_classes_to_run = [TestDPLL, TestDPLL]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)