# Author: jkk.lapp@gmail.com, 2015

import sys
from random import randint

class Tester:

	def __init__(self):
		self.colors_to_inspect = []

	def update_colors_to_inspect(self, satisfaction, customers):
		for i in range(len(satisfaction)):
			if not satisfaction[i]:
				for t in customers[i]:
					color = int(t[0])
					if color not in self.colors_to_inspect:
						self.colors_to_inspect.append(color)


	'''
		Checks if a solution satisfies for a given case
		of customer types.

		Args:
			* solution: A list containing a solution.
			* customers: A list containing customers types.
		Returns:
			True if the solution satisfies the list of customers.
			False otherwise.
	'''
	def is_valid_solution(self, solution, customers):
		customer_satisfaction = [False for i in range(len(customers))]
		already_sold = []
		for i in range(len(customers)):
			c = customers[i]
			for type in c:
				type = type.split()
				tone = int(type[0]) - 1
				variety = int(type[1])
				if variety == solution[tone] and tone not in already_sold:
					already_sold.append(tone)
					customer_satisfaction[i] = True
					continue
		self.already_sold = [i + 1 for i in already_sold]
		self.update_colors_to_inspect(customer_satisfaction, customers)
		return False not in customer_satisfaction

