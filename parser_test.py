# Author: jkk.lapp@gmail.com, 2015

import unittest
from parser import Parser
from generator import Generator
import os

class TestParser(unittest.TestCase):

	def setUp(self):
		self.max_n = 50
		self.max_m = 50
		self.gen = Generator(self.max_n, self.max_m)
		self.n_cases = 10
		self.gen.generate_test_cases(self.n_cases)
		self.gen.print_test_cases_to_file(self.n_cases, 'testfile')
		self.parser = Parser('testfile')

	def test_read_next_case(self):
		for i in range(self.n_cases):
			c = self.parser.read_next_case()
			self.assertTrue(len(c) < (self.max_m + 1))
		no_case = self.parser.read_next_case()
		self.assertIsNone(no_case)
		no_case = self.parser.read_next_case()
		self.assertIsNone(no_case)


	def tearDown(self):
		os.remove('testfile')


if __name__ == '__main__':
    unittest.main()