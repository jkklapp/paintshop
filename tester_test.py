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
		self.customers6 = [['2 0']]
		self.customers7 = [['1 0']]
		self.customers8 = [['3 0', '1 1', '2 0']]
		self.customers9 = [['1 0', '2 0'], ['1 1', '2 0'], ['1 0']]
		self.customers10 = [['2 1', '1 0'], ['2 1', '1 0']]
		self.customers11 = [['2 0', '1 0'], ['1 0']]
		self.customers12 = [['3 1', '2 0'], ['2 1'], ['2 1', '1 0']]
		self.customers13 = [['2 1', '1 0'], ['2 0', '1 1']]
		self.customers14 = [['3 0'], ['2 1', '1 0', '3 0']]
		self.solution1 = [0, 0, 0]
		self.solution2 = [1, 0, 0]
		self.solution3 = [0, 1, 0]
		self.solution4 = [1, 1, 1]
		self.solution5 = [0, 0]
		self.solution6 = [0]
		self.solution7 = [0, 1]
		self.solution8 = [1, 0, 0]
		self.solution9 = [0, 1, 1]
		self.solution10 = [0, 0, 1]
		self.solution11 = [1, 1, 1]
		self.solution12 = [1, 1, 0]

	def test_solution_tester(self):
		is_valid = self.tester.is_valid_solution
		c1 = self.customers1
		c2 = self.customers2
		c3 = self.customers3
		c4 = self.customers4
		c5 = self.customers5
		c6 = self.customers6
		c7 = self.customers7
		c8 = self.customers8
		c9 = self.customers9
		c10 = self.customers10
		c11 = self.customers11
		c12 = self.customers12
		c13 = self.customers13
		c14 = self.customers14
		s1 = self.solution1
		s2 = self.solution2
		s3 = self.solution3
		s4 = self.solution4
		s5 = self.solution5
		s6 = self.solution6
		s7 = self.solution7
		s8 = self.solution8
		s9 = self.solution9
		s10 = self.solution10
		s11 = self.solution11
		s12 = self.solution12
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
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s1, c6))
		self.assertFalse(self.tester.impossible)
		self.assertTrue(is_valid(s5, c6))
		self.assertTrue(is_valid(s1, c7))
		self.assertFalse(is_valid(s3, c7))
		self.assertTrue(is_valid(s5, c7))
		self.assertTrue(is_valid(s6, c7))
		self.assertTrue(is_valid(s7, c7))
		self.assertTrue(is_valid(s8, c8))
		self.assertFalse(is_valid(s1, c9))
		self.assertTrue(self.tester.impossible)
		self.assertTrue(is_valid(s3, c10))
		self.assertTrue(is_valid(s9, c10))
		self.assertTrue(is_valid(s1, c11))
		self.assertTrue(is_valid(s5, c11))
		self.assertTrue(is_valid(s10, c11))
		self.assertFalse(is_valid(s11, c12))
		self.assertTrue(is_valid(s9, c12))
		self.assertTrue(is_valid(s12, c13))
		self.assertTrue(is_valid(s1, c13))
		self.assertTrue(is_valid(s1, c14))
		self.assertTrue(is_valid(s3, c14))
		self.assertTrue(is_valid(s12, c14))




if __name__ == '__main__':
    unittest.main()