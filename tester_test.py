# Author: jkk.lapp@gmail.com, 2015

import unittest
from tester import Tester

class TestTester(unittest.TestCase):

	def setUp(self):
		self.tester = Tester()
		self.customers1 = [['1 0', '2 0'], ['1 1'], ['3 0']]
		self.customers2 = [['1 0', '2 1'], ['1 1'], ['3 1']]
		self.customers3 = [['2 0', '1 0'], ['2 1', '1 0']]
		self.customers4 = [['2 1', '1 0'], ['2 1']]
		self.customers5 = [['2 0', '1 0'], ['2 0', '1 1']]
		self.solution1 = [0, 0, 0]
		self.solution2 = [1, 0, 0]
		self.solution3 = [0, 1, 0]
		self.solution4 = [1, 1, 1]
		self.solution5 = [0, 0]
		self.solution6 = [0]
		self.solution7 = [0, 1]



	def test_solution_tester(self):
		is_valid = self.tester.is_valid_solution
		c1 = self.customers1
		c2 = self.customers2
		c3 = self.customers3
		c4 = self.customers4
		c5 = self.customers5
		s1 = self.solution1
		s2 = self.solution2
		s3 = self.solution3
		s4 = self.solution4
		s5 = self.solution5
		s6 = self.solution6
		s7 = self.solution7
		self.assertFalse(is_valid(s1, c1))
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s2, c1))
		self.assertFalse(self.tester.impossible)
		self.assertFalse(is_valid(s3, c1))
		self.assertFalse(self.tester.impossible)
		self.assertFalse(is_valid(s3, c2))
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s4, c2))
		self.assertFalse(self.tester.impossible)
		self.assertFalse(is_valid(s4, c1))
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s5, c3))
		self.assertFalse(self.tester.impossible)
		self.assertFalse(is_valid(s6, c3))
		self.assertTrue(self.tester.impossible)
		self.assertFalse(is_valid(s5, c4))
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s7, c4))
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s5, c5))




if __name__ == '__main__':
    unittest.main()