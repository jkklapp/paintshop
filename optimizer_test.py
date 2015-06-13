# Author: jkk.lapp@gmail.com, 2015

import unittest
from optimizer import Optimizer

class TestOptimizer(unittest.TestCase):

	def setUp(self):
		self.opt = Optimizer(['0', '0', '0'], [['1 0', '2 0'], ['1 1'], ['3 0']])

	def test_matte_minimizer(self):
		self.opt.matte_minimizer()
		self.assertEqual(self.opt.steps, 1)
		self.assertEqual(self.opt.solution, ['1', '0', '0'])
		self.opt.solution = ['0', '0', '0']
		self.opt.case = [['1 1', '2 1'], ['1 0'], ['3 0']]
		self.opt.matte_minimizer()
		self.assertEqual(self.opt.steps, 3)
		self.assertEqual(self.opt.solution, ['0', '1', '0'])

	def test_random_optimizer(self):
		self.opt.solution = ['0', '0', '0', '0']
		self.opt.case = [['1 1', '2 1', '3 0'], ['1 0', '3 1'], ['3 0', '4 1'], ['2 0', '4 0']]
		self.opt.random_optimizer(16)
		s = self.opt.solution
		# Two possible solutions, [1, 0, 1, 1] and [0, 0, 0, 1]
		self.assertEqual(s[1], '0')
		self.assertEqual(s[3], '1')
		self.assertEqual(s[0], s[2])
		s = self.opt.solution
		# Make sure we have improved the answer
		self.assertEqual(s[0], '0')	


if __name__ == '__main__':
    unittest.main()