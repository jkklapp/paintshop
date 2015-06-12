# Author: jkk.lapp@gmail.com, 2015

from tester import Tester
from random import randint

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
		self.case = case
		self.tester = Tester()
		self.steps = 0

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
		return [0 for i in range(n)]

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
		solution[i] += 1
		solution[i] = solution[i] % 2
		return solution

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
	def random_optimizer(self):
		solution = self.solution
		tester = self.tester
		case = self.case
		i = 0
		while not tester.is_valid_solution(solution, case):
			solution = self.change_solution(solution, randint(0, len(solution) - 1))
			i += 1
		self.steps = i
		self.solution = solution

	'''
		Tries to improve a solution incrementally.

		This method generates a solution that satisfies, and
		then tries to turn 1s into 0s until it no longer satisfies.

		Args:
			solution: A solution candidate. None will use the optimal naive solution.
		Returns
			The first solution that satisfies.
	'''
	def matte_minimizer(self):
		solution = self.solution
		tester = self.tester
		case = self.case
		i = 0
		while i < len(solution):
			solution = self.change_solution(solution, i)
			i += 1
			if not tester.is_valid_solution(solution, case):
				solution = self.change_solution(solution, i-1)
			else:
				break
		self.steps = i
		self.solution = solution


	'''
		Looks only into specific colors to get a better solution

		This method generates a solution that satisfies, and
		then tries to turn 1s into 0s until it no longer satisfies.

		Args:
			solution: A solution candidate. None will use the optimal naive solution.
		Returns
			The first solution that satisfies.
	'''
	def targeted_color_optimizer(self):
		solution = self.solution
		tester = self.tester
		case = self.case
		print tester.colors_to_inspect
		print tester.already_sold
		i = 0
		for j in tester.colors_to_inspect:
			if j in tester.already_sold:
				continue
			solution = self.change_solution(solution, j-1)
			i += 1
			if not tester.is_valid_solution(solution, case):
				solution = self.change_solution(solution, j-1)
			else:
				break
		self.steps = i
		self.solution = solution

	'''
		Executes the optmization:
	'''
	def optimize(self, method='random_optimizer'):
		self.method(self.solution)

	'''
		Prints results
	'''
	def get_solution(self):
		tester = self.tester
		if tester.is_valid_solution(self.solution, self.case):
			return " ".join(self.solution)
		else:
			return "IMPOSSIBLE"
