# Author: jkk.lapp@gmail.com, 2015

import sys
from random import randint

'''
	Reads a case from a case file.

	One line containing the N number of colors in the case.
	One line containing the M number of customers in the case.
	M lines each one containing the types for each customer.

	Args:
		* f: A file Object.
	Returns:
		A list containing the customer types, e.g.:
			[['1 0', '2 1'], ['1 1'], ['3 0']]
'''
def read_case(f):
	n = int(f.readline())
	m = int(f.readline())
	customers = []
	for i in range(m):
		customers.append(read_customer_types(f.readline()))
	return customers

'''
	Parses a customer's type from the file.

	Args:
		* t: A type String.
	Returns:
		A list containing the customer type, e.g.:
			['1 0', '2 1']
'''
def read_customer_types(t):
	raw_list = t.split()
	return [[raw_list[i], raw_list[i + 1]] for i in range(2, len(raw_list) - 1)]

'''
	Checks if a solution satisfies for a given case
	and a set of customer types.

	Args:
		* solution: A list containing a solution.
		* customers: A list containing customers types.
	Returns:
		True if the solution satisfies the list of customers.
		False otherwise.
'''
def solution_tester(solution, customers):
	customer_satisfaction = [False for i in range(len(customers))]
	already_sold = []
	for i in range(len(customers)):
		c = customers[i]
		for type in c:
			tone = int(type[0]) - 1
			variety = int(type[1])
			if variety == solution[tone] and tone not in already_sold:
				already_sold.append(tone)
				customer_satisfaction[i] = True
				continue
	return False not in customer_satisfaction

if __name__ == '__main__':
	# Check if the solution is provided by cmd line.
	print len(sys.argv)
	if len(sys.argv) > 3:
		solution = [int(t) for t in sys.argv[4].split()]
	else:
		solution = [randint(0, 1) for i in range(int(sys.argv[2]))]
	if len(solution) < int(sys.argv[2]):
		print '''The solution must contain at least the same number of max colors
		the customers may require.'''
	else:
		# Read file
		filename = sys.argv[1]
		with open(filename, 'r') as f:
			n_cases = int(f.readline())
			for i in range(n_cases):
				customers = read_case(f)
				if not solution_tester(solution, customers):
					print "Case #" + str(i + 1) + ": IMPOSSIBLE"
				else:
					print "Case #" + str(i + 1) + ": " + " ".join([str(x) for x in solution])
