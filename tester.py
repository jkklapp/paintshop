# Author: jkk.lapp@gmail.com, 2015

import sys
from random import randint

class Tester:

	def __init__(self):
		self.colors_to_inspect = []
		self.impossible = False

	def update_colors_to_inspect(self, satisfaction, customers):
		for i in range(len(satisfaction)):
			if not satisfaction[i]:
				for t in customers[i]:
					color = int(t[0])
					if color not in self.colors_to_inspect:
						self.colors_to_inspect.append(color)


	'''
		Checks if two customers want the same color
		and only one color.
	'''
	def customer_collission(self, solution, customers):
		if len(customers) == 1:
			return False
		only_want_1_color = [len(c) == 1 for c in customers]
		if False not in only_want_1_color:
			colors = [t[0][0] for t in customers]
			return len(list(set(colors))) == 1

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
		# Breaking conditions
		# If there are less colors that customers)
		if len(solution) < len(customers):
			self.impossible = True
			return False
		# If two customers only want 1 color, the same color.
		if self.customer_collission(solution, customers):
			self.impossible = True
			return False
		self.impossible = False
		already_sold = []
		i = 0
		customers = sorted(customers, lambda x,y: 1 if len(x)>len(y) else -1 if len(x)<len(y) else 0)
		while i < len(customers):
			c = customers[i]
			for type in c:
				type = type.split()
				tone = int(type[0]) - 1
				variety = int(type[1])
				if variety == solution[tone] and tone not in already_sold:
					already_sold.append(tone)
					customer_satisfaction[i] = True
					break
			i += 1
		print customers
		print customer_satisfaction
		self.already_sold = [i + 1 for i in already_sold]
		self.update_colors_to_inspect(customer_satisfaction, customers)
		return False not in customer_satisfaction

