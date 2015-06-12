# Author: jkk.lapp@gmail.com, 2015

import sys
from random import randint

class Parser:
	'''
		Checks if a solution satisfies a 
		provided test case.

	'''
	def __init__(self, filename):
		self.f = open(filename, 'r')
		self.c = int(self.f.readline())

	'''
		Close the file.
	'''
	def finish(self):
		self.f.close()

	'''
		Reads the next case from a case file.

		One line containing the N number of colors in the case.
		One line containing the M number of customers in the case.
		M lines each one containing the types for each customer.

		Args:
			* f: A file Object.
		Returns:
			A list containing the customer types, e.g.:
				[['1 0', '2 1'], ['1 1'], ['3 0']]
	'''
	def read_next_case(self):
		if self.c == 0:
			self.finish()
			return None
		n = int(self.f.readline())
		m = int(self.f.readline())
		customers = []
		for i in range(m):
			customers.append(self.read_customer_types(self.f.readline()))
		self.c -= 1
		return customers

	'''
		Parses a customer's type from the file.

		Args:
			* t: A type String.
		Returns:
			A list containing the customer type, e.g.:
				['1 0', '2 1']
	'''
	def read_customer_types(self, t):
		raw_list = t.split()
		l = [raw_list[i] + " " + raw_list[i + 1] for i in range(1, len(raw_list), 2)]
		return l
