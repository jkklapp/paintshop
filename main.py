# Author: jkk.lapp@gmail.com, 2015

from generator import Generator
from tester import Tester
from parser import Parser
from optimizer import Optimizer

import sys, os

if __name__ == '__main__':
	# Check if the solution is provided by cmd line.

	if len(sys.argv) not in [4, 5]:
		print '''Usage: ./main.py <# test cases> <max #colors> <max # customers> [optimization_method]'''
	else:
		# Write file
		max_n = int(sys.argv[2])
		max_m = int(sys.argv[3])
		c = int(sys.argv[1])
		method = sys.argv[4] if len(sys.argv) == 5 else 'random_optimizer'
		print "Using " + method + " method to find and optimize a solution."
		gen = Generator(max_n, max_m)
		gen.generate_test_cases(c)
		gen.print_test_cases(c)
		gen.print_test_cases_to_file(c, 'testfile')
		parser = Parser('testfile')
		opt = Optimizer([0 for i in range(max_n)], [])
		for i in range(c):
			opt.case = parser.read_next_case()
			opt.optimize(method)
			print "Case #" + str(i + 1) + ": " + opt.get_solution()
		os.remove('testfile')
