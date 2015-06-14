# Author: jkk.lapp@gmail.com, 2015

from itertools import permutations

class Tester:

	def __init__(self):
		self.impossible = False

	'''
		Generates all possible permutations of customers

		Args:
			* solution: A list containing a solution.
			* customers: A list containing customers types.
		Returns:
			True if the solution satisfies the list of customers.
			False otherwise.
	'''
	def is_valid_solution(self, solution, customers):
		if len(solution) < len(customers):
			self.impossible = True
			return False
		for perm in list(permutations(customers)):
			if self.check_solution_for_perm(solution, perm):
				return True
		return False

	'''
		Checks if a solution is in all possible solutions.

		Args:
			* solution: A list containing a solution.
			* customers: A list containing customers types.
		Returns:
			True if the solution satisfies the list of customers.
			False otherwise.
	'''
	def check_solution_for_perm(self, solution, customers):
		self.impossible = False
		customer_satisfaction = [False for i in range(len(customers))]
		already_sold = []
		for i in range(len(customers)):
			c = customers[i]
			for type in c:
				type = type.split()
				tone = int(type[0]) - 1
				variety = type[1]
				if variety == solution[tone] and tone not in already_sold:
					already_sold.append(tone)
					customer_satisfaction[i] = True
					break
		return False not in customer_satisfaction


