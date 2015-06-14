# Author jkk.lapp@gmail.com, 2015
from itertools import product
from itertools import groupby
from itertools import combinations_with_replacement as comb

class Solver:

	def __init__(self, length, customers):
		self.impossible = False
		self.solutions = []
		self.customers = customers
		self.length = length
	
	'''
		Sorts customer types by color in ascending order.
	'''
	def sort_types(self, x, y):
		return 1 if int(x.split()[0]) > int(y.split()[0]) else -1

	'''
		Expands a candidate solution to the max number of
		colors.
	'''
	def merge_with_expanded(self, candidate, expanded_candidates):
		for t in candidate:
			i = int(t.split()[0]) - 1
			variety = t.split()[1]
			for e in expanded_candidates:
				e[i] = variety
		return expanded_candidates


	'''
	'''
	def get_rid_of_useless_products(self, products):
		filtered_products = []
		for p in products:
			colors_in_product = [x.split()[0] for x in p]
			if len(colors_in_product) == len(set(colors_in_product)):
				filtered_products.append(p)
		return filtered_products

	'''
		Get best solution
	'''
	def get_optimal_solution(self):
		if not self.solutions:
			self.compute_solutions(self.customers)
		sols = self.solutions
		for i in range(self.length):
			for s in sols:
				total = sum(int(x) for x in s)
				if total == i:
					return s

	'''
		Generates all valid solutions

		Args:
			* customers: A list containing customers types.
			* length: Length of the solutions.

		Returns:
			A list with all possible solutions.
	'''
	def compute_solutions(self, customers=None):
		if not customers:
			customers = self.customers
		length = self.length
		if length < len(customers):
			self.impossible = True
			self.solutions.append("IMPOSSIBLE")
			return False
		self.impossible = False
		products = [list(y) for y in [x for x in product(*customers)]]
		p = self.get_rid_of_useless_products(products)
		all_possible_sols = []
		for candidate in p:
			expanded_candidates = [list(x) for x in comb(('0', '1'), length)]
			new_candidates = self.merge_with_expanded(candidate, expanded_candidates)
			for new_candidate in new_candidates:
				if new_candidate not in all_possible_sols:
					all_possible_sols.append(new_candidate)
		self.solutions = all_possible_sols