# Author: jkk.lapp@gmail.com, 2015

import unittest
from solver import Solver

class TestSolver(unittest.TestCase):

	def setUp(self):
		self.solver = Solver(0, [])

	def test_solver_small(self):
		self.solver.length = 2
		self.solver.customers = [['1 1', '2 0'], ['1 0', '2 1']]
		s1 = ['0', '0']
		s2 = ['1', '1']
		self.solver.compute_solutions()
		sols = self.solver.solutions
		self.assertIn(s1, sols)
		self.assertIn(s2, sols)
		optimal = self.solver.get_optimal_solution()
		self.assertEqual(optimal[0], '0')
		self.assertEqual(optimal[1], '0')
		

	def test_solver_medium3(self):
		self.solver.length = 5
		self.solver.customers = [['1 1'], ['1 0', '2 0'], ['5 0'], ['2 1', '3 0']]
		self.solver.compute_solutions()
		sols = self.solver.solutions
		s = ['1', '0', '0', '0', '0']
		self.assertEqual(len(sols), 1)
		self.assertIn(s, sols)

	def test_solver_medium1(self):
		self.solver.customers = [['1 0', '6 1', '3 0', '4 0'],
			['5 1', '2 0', '3 0', '6 0'],
			['1 0', '5 1', '3 0', '4 0', '6 0'],
			['2 1'], ['2 1', '1 0', '6 0', '3 0']]
		self.solver.length = 6
		self.solver.compute_solutions()
		sols = self.solver.solutions
		self.assertEqual(len(sols), 3)
		optimal = self.solver.get_optimal_solution()
		self.assertEqual(optimal[0], '0')
		self.assertEqual(optimal[1], '1')
		self.assertEqual(optimal[2], '0')
		self.assertEqual(optimal[3], '0')
		self.assertEqual(optimal[4], '0')
		self.assertEqual(optimal[5], '0')


	def test_solver_medium2(self):
		self.solver.length = 5
		self.solver.customers = [['1 1', '2 0', '4 0'],
								 ['2 1', '1 0'],
								 ['2 1', '3 0'],
								 ['3 1', '2 0'],
								 ['4 1', '5 0'],
								 ['5 1']]
		self.solver.compute_solutions()
		self.assertTrue(self.solver.impossible)


	def test_solver_medium4(self):
		self.solver.length = 5
		self.solver.customers = [['1 1', '2 0', '4 0'],
			['2 1', '3 0'], ['3 1', '1 0'],
			['4 1', '5 0'], ['5 1']]
		s1 = ['1', '1', '1', '1', '1']
		s2 = ['0', '0', '0', '1', '1']
		self.solver.compute_solutions()
		sols = self.solver.solutions
		self.assertEqual(len(sols), 2)
		self.assertIn(s1, sols)
		self.assertIn(s2, sols)
		optimal = self.solver.get_optimal_solution()
		self.assertEqual(s2, optimal)


	def test_expansion(self):
		expand = self.solver.expand_a_candidate
		self.solver.length = 5
		candidate1 = ['1 1', '1 0', '5 0', '1 1', '3 1']
		self.assertIsNone(expand(candidate1))
		candidate2 = ['1 1', '2 0', '5 0']
		self.assertEqual(expand(candidate2), ['1 1', '2 0', '3 0', '4 0', '5 0'])
		candidate3 = ['1 1', '1 0', '5 0']
		self.assertIsNone(expand(candidate3))
		candidate4 = ['1 1', '1 0', '5 0', '2 1']
		self.assertIsNone(expand(candidate4))


if __name__ == '__main__':
    unittest.main()