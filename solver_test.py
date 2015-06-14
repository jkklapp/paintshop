# Author: jkk.lapp@gmail.com, 2015

import unittest
from solver import Solver

class TestSolver(unittest.TestCase):

	def setUp(self):
		self.customers1 = [['2 1', '1 0'], ['2 0', '1 1']]
		self.solver = Solver(2, self.customers1)
		self.solution1 = ['0', '0']
		self.solution2 = ['1', '1']
		

	def test_solver(self):
		s1 = self.solution1
		s2 = self.solution2
		self.solver.compute_solutions()
		sols = self.solver.solutions
		self.assertIn(s1, sols)
		self.assertIn(s2, sols)
		optimal = self.solver.get_optimal_solution()
		self.assertEqual(optimal[0], '0')
		self.assertEqual(optimal[1], '0')
		self.solver.customers = [['1 0', '6 1', '3 0', '4 0'],
			['5 1', '2 0', '3 0', '6 0'], ['1 0', '5 1', '3 0', '4 0', '6 0'],
			['2 1'], ['2 1', '1 0', '6 0', '3 0']]
		self.solver.length = 6
		self.solver.compute_solutions()
		sols = self.solver.solutions
		self.assertEqual(len(sols), 10)
		optimal = self.solver.get_optimal_solution()
		self.assertEqual(optimal[0], '0')
		self.assertEqual(optimal[1], '1')
		self.assertEqual(optimal[2], '0')
		self.assertEqual(optimal[3], '0')
		self.assertEqual(optimal[4], '0')
		self.assertEqual(optimal[5], '0')


if __name__ == '__main__':
    unittest.main()