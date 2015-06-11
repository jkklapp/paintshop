# Author: jkk.lapp@gmail.com, 2015

import sys
from random import randint
from random import sample

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
def generate_test_case(n, m):
	pool_of_total_requests = 3000
	customers = []
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
		customers.append(str(n_customer_types) + type_of_color)
	return customers

'''
	Prints a test case.

	Args:
		case: A case string.
		n: The number of colors in the case.
		m: The number of customers in the case.
	Returns:
		None
'''
def print_case(case, n, m):
	print n
	print m
	for t in case:
		print t


if __name__ == "__main__":
	c = int(sys.argv[1])
	max_n = int(sys.argv[2])
	max_m = int(sys.argv[3])
	print c
	for i in range(c):
		n = randint(1, max_n)
		m = randint(1, max_m)
		case = generate_test_case(n, m)
		print_case(case)



