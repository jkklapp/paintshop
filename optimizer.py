# Author: jkk.lapp@gmail.com, 2015

from tester import Tester
from random import randint
from math import pow

class Optimizer:
	"""
		Object that implements different
		optimization strategies for a solution.

		Attrs:
			solution: A solution being optimized.
			case: A list of customers with their requirements.
	"""
	def __init__(self, solution, case):
		self.solution = solution
		self.current_mattes = sum([int(x) for x in solution])
		self.case = case
		self.tester = Tester()
		self.valid_solution = False
		self.steps = 0
		self.METHODS = {
			'random_optimizer': self.random_optimizer,
			'matte_minimizer': self.matte_minimizer
		}

	'''
		Generates the optimal naive solution.

		The optimal solution is to produce a batch
		of each color glossy.

		[0, 0, ..., 0]

		Args:
			n: The number of colors.
		Returns:
			A list of n 0s. 
	'''
	def generate_naive_solution(self, n):
		return ['0' for i in range(n)]

	'''
		Modifies a solution.

		Args:
			solution: An array with 0s and 1s.
			i: Position to switch value.
		Returns
			The same solution with the i-th 
			position switched.
	'''
	def change_solution(self, solution, i):
		solution[i] = '1' if solution[i] == '0' else '0'
		return solution

	'''
		Checks if the solution has improved

		Args:
			solution: An array with 0s and 1s.

		Returns:
			True if the solution is still valid
			and the number of 1s has decreased.
			False otherwise.
	'''
	def solution_improved(self, s):
		candidate_mattes = sum([int(x) for x in s])
		if self.valid_solution and candidate_mattes < self.current_mattes:
			self.current_mattes = candidate_mattes
			return True
		return False

	'''
		Uses inspection to optimize randomly a solution.

		The idea is to switch the value of random positions in the
		solution array and check if the solution satisfies. Does
		nothing if the solution already satisfies.

		Args:
			solution: A solution candidate.
		Returns
			The first solution that satisfies
	'''
	def random_optimizer(self, i=1):
		tester = self.tester
		case = self.case
		s = self.solution
		for k in range(i):
			self.valid_solution = self.tester.is_valid_solution(self.solution, case)
			pos = randint(0, len(solution)-1)
			s = self.change_solution(s, pos)			
			if self.solution_improved(s):
				self.solution = s
			else:
				s = self.change_solution(s, pos)
		self.steps += i

	'''
		Tries to improve a solution incrementally.

		This method generates a solution that satisfies, and
		then tries to turn 1s into 0s until it no longer satisfies.

		Args:
			solution: A solution candidate. None will use the optimal naive solution.
		Returns
			The solution that satisfies with the least number of 1s.
	'''
	def matte_minimizer(self):
		solution = self.solution
		tester = self.tester
		case = self.case
		i = 0
		while i < len(solution):
			solution = self.change_solution(solution, i)
			self.valid_solution = tester.is_valid_solution(solution, case)
			if self.solution_improved(solution):
				self.solution = solution
			else:
				solution = self.change_solution(solution, i)
			i += 1
		self.steps = i

	'''
		Executes the optmization:

		Args:
			method: The name of your optimization method.
	'''
	def optimize(self, method=None):
		if not method:
			method = 'random_optimizer'
		self.valid_solution = self.tester.is_valid_solution(self.solution, self.case)
		self.steps = 0
		if not self.tester.impossible:
			self.METHODS[method]()

	'''
		Prints results
	'''
	def get_solution(self):
		tester = self.tester
		if (self.tester.impossible):
			return "IMPOSSIBLE"
		else:
			return " ".join([str(s) for s in self.solution])
		
