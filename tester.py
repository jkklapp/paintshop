# Author: jkk.lapp@gmail.com, 2015

import sys
from itertools import product
from itertools import groupby
from itertools import combinations_with_replacement as comb
from random import randint

class Tester:

	def __init__(self):
		self.impossible = False

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
		Gets the number of different colors in a 
		customer list.
	'''
	def get_number_of_colors(self, customers):
		l = []
		for c in customers:
			l += c
		l = [int(c.split()[0]) for c in l]
		return max(l)

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
		colors = self.get_number_of_colors(customers)
		if colors < len(customers) or len(solution) < len(customers):
			self.impossible = True
			return False
		self.impossible = False
		sorted_customers = []
		for c in customers:
			sorted_c = sorted(c, lambda x, y: 1 if x.split()[0] > y.split()[0] else -1)
			sorted_customers.append(sorted_c)
		customers = sorted_customers
		products = [list(y) for y in [x for x in product(*customers)]]
		p = self.get_rid_of_useless_products(products)
		all_possible_sols = []
		for candidate in p:
			expanded_candidates = [list(x) for x in comb(('0', '1'), len(solution))]
			all_possible_sols += self.merge_with_expanded(candidate, expanded_candidates)
		if len(all_possible_sols) == 0:
			self.impossible = True
		return solution in all_possible_sols


