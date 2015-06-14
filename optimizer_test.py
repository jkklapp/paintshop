# Author: jkk.lapp@gmail.com, 2015

import unittest
from optimizer import Optimizer

class TestOptimizer(unittest.TestCase):

	def setUp(self):
		self.opt = Optimizer(['1', '1', '1'],
							 [['1 1', '2 0', '3 1'], ['1 0', '2 1', '3 1'], ['1 0', '3 0', '2 1']])

	def test_matte_minimizer(self):
		self.opt.matte_minimizer()
		self.assertEqual(self.opt.solution, ['0', '0', '0'])
		self.assertEqual(self.opt.steps, 3)

if __name__ == '__main__':
    unittest.main()