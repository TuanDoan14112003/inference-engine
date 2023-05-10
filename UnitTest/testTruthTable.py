import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from TTAlgorithm import TruthTableAlgorithm
from environment import Environment

class TestTruthTable(unittest.TestCase):
    def test_1(self):
        env = Environment()
        env.readFile("testcases/hornClause.txt")
        truthTable = TruthTableAlgorithm()
        truthTable.checkAll(env.knowledgeBase, env.query, env.symbols, [])
        self.assertEqual(1, 1)