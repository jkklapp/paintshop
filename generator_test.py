# Author: jkk.lapp@gmail.com, 2015

import unittest
from generator import Generator
import sys

class TestGenerator(unittest.TestCase):

	def setUp(self):
		self.gen = Generator(3, 3)

	def test_generate_test_cases(self):
		self.gen.generate_test_cases(1)
		self.assertEqual(len(self.gen.cases), 1)
		self.gen.generate_test_cases(4)
		self.assertEqual(len(self.gen.cases), 5)

	def test_generate_test_case(self):
		t = self.gen.generate_test_case(1, 1)
		self.assertEqual(len(t), 3)
		self.assertEqual(t[0], 1)
		self.assertEqual(t[1], 1)
		self.assertTrue(len(t[2]) < 5)

if __name__ == '__main__':
    unittest.main()