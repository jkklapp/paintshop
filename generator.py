# Author: jkk.lapp@gmail.com, 2015

from random import randint
from random import sample

class Generator:
	'''
		A case set generator.

		Generates test cases with maximum N and M

		Attrs:
			c: The cases to generate
			max_n: The maximum number of colors in the case
			max_m: The maximum number of customers in the case. 
	'''
	def __init__(self, max_n, max_m):
		self.max_n = max_n
		self.max_m = max_m
		self.cases = []

	'''
		Helper that prints a case

	'''
	def print_case(self, case, n, m):
		print n
		print m
		for t in case:
			print t

	'''
		Generates a test case.

		For N colors, generates a test case for M
		customers, providing the total number of types
		for the M customers is not bigger than 3000 and
		for each customer variety == 1 only once.

		Args:
			n: An integer for the number of colors.
			m: An integer for the number of customers.
		Returns:
			A list of strings like
			["number_of_types0 color1 variety0 color2 variety1 ...",
			 "number_of_types1 color3 variety1 colorN variety0 ...", 
			 ...,
			 "number_of_typesn-1 colorN variety0 colorN-2 variety1 ..."]
	'''
	def generate_test_case(self, n, m):
		pool_of_total_requests = 3000
		case = []
		for i in range(m):
			n_customer_types = randint(1, n)
			pool_of_total_requests -= n_customer_types
			if pool_of_total_requests <= 0:
				break
			type_of_color = ""
			already_chosen_matte = False
			customer_choices = sample(range(1, n + 1), n_customer_types)
			for j in customer_choices:
				if already_chosen_matte:
					variety = 0
				else:
					variety = randint(0, 1)
					if variety == 1:
						already_chosen_matte = True
				type_of_color += " " + str(j) + " " + str(variety)
			case.append(str(n_customer_types) + type_of_color)
		return [n, m, case]


	'''
		Generate c test cases.
	'''
	def generate_test_cases(self, c):
		for i in range(c):
			n = randint(1, self.max_n)
			m = randint(1, self.max_m)
			test_case = self.generate_test_case(n, m)
			self.cases.append(test_case)

	'''
		Prints c test cases.
	'''
	def print_test_cases(self, c):
		print c
		for i in range(len(self.cases)):
			n = self.cases[i][0]
			m = self.cases[i][1]
			case = self.cases[i][2]
			self.print_case(case, n, m)

	'''
		Generates and prints c test cases.
	'''
	def generate_and_print_test_cases(self, c):
		self.generate_test_cases(c)
		self.print_test_cases(c)

	'''
		Prints output to a file
	'''
	def print_test_cases_to_file(self, c, filename):
		f = open(filename, 'w')
		f.write(str(c) + '\n')
		for i in range(len(self.cases)):
			n = self.cases[i][0]
			m = self.cases[i][1]
			case = self.cases[i][2]
			f.write(str(n) + '\n')
			f.write(str(m) + '\n')
			for t in case:
				f.write(t + '\n')
		f.close()


