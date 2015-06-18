# Author jkk.lapp@gmail.com, 2015
from itertools import product
from itertools import groupby
from itertools import combinations_with_replacement as comb

class Solver:

	def __init__(self, length, customers, get_the_first=False):
		self.impossible = False
		self.solutions = []
		self.customers = customers
		self.length = length
		self.return_first = get_the_first
	
	'''
		Get best solution

		Returns:
			The solution with least number of 1s.
	'''
	def get_optimal_solution(self):
		if not self.solutions:
			self.compute_solutions(self.customers)
		if self.impossible:
			return "IMPOSSIBLE"
		sols = self.solutions
		for i in range(0, self.length+1):
			for s in sols:
				total = sum(int(x) for x in s)
				if total == i:
					return s

	'''
		Get a random solution

		Returns:
			The first solution in the solutions list.
	'''
	def get_random_solution(self):
		if not self.solutions:
			self.compute_solutions(self.customers)
		if self.impossible:
			return "IMPOSSIBLE"
		return self.solutions[0]

	'''
		Tells if an expansion was valid

		If the candidate is invalid it can be detected 
		in each step of the expansion..

		Returns:
			True if it is valid, False otherwise
	'''
	def invalid_expansion_detected(self, expanded, insertion):
		index = expanded.index(insertion)
		if len(expanded) > 2 and index != len(expanded) - 1 and index != 0:
			return expanded[index-1][0] == expanded[index+1][0]

	'''
		Expands a candidate to the length of a 
		solution

		Args:
			c: A simple candidate from a product.

		Returns:
			The candidate with 0 for the colors
			that were not present originally.

	'''
	def expand_a_candidate(self, candidate):
		expanded = []
		for t in candidate:
			index = int(t[0]) - 1
			expanded.insert(index, t)
			if self.invalid_expansion_detected(expanded, t):
				return None
		for i in range(1, self.length):
			if expanded[i-1][0] != str(i):
				insertion = str(i) + " 0"
				expanded.insert(i-1, insertion)
				if self.invalid_expansion_detected(expanded, insertion):
					return None
		if len(expanded) != self.length:
			return None
		return expanded

	'''
		Gets the varieties of a candidate

		Args:
			c: A valid candidate with types
			in order.

		Returns:
			A list of varieties.
	'''
	def candidate_to_solution(self, c):
		return [x.split()[1] for x in c]

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
			return False
		self.impossible = False
		self.solutions = []
		for p in product(*customers):
			p = list(p)
			p = self.expand_a_candidate(p)
			if not p:
				continue
			p = self.candidate_to_solution(p)
			if p not in self.solutions:						
				self.solutions.append(p)
				if self.return_first:
					return True
		if not self.solutions:
			self.impossible = True
			return False
