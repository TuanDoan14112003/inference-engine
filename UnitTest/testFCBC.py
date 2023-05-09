from environment import Environment
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from forwardChainingAlgorithm import ForwardChaining
from backwardChainingAlgorithm import BCAlgorithm
from testGenerator import TestGenerator



class TestFCBC(unittest.TestCase):
    def test_1(self):
        testGenerator = TestGenerator()
        testGenerator.generateHornCase("testcases/hornClause")
        for i in range(1,10):
            env = Environment()
            env.readFile("testcases/hornClause"+str(i)+".txt")
            forwardChaining = ForwardChaining()
            backwardChaining = BCAlgorithm()
            self.assertEqual(forwardChaining.forwardChainingEntails(
                env.knowledgeBase, env.symbols, env.query), 
                backwardChaining.backwardChainingEntails(env.knowledgeBase, env.symbols, env.query))


    

if __name__ == "__main__":
    unittest.main()
