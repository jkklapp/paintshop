# Author: jkk.lapp@gmail.com, 2015

from generator import Generator
from solver import Solver
from tester import Tester
from parser import Parser
from optimizer import Optimizer

import sys, os, argparse


def write_case(c, n, m, f=None):
	gen = Generator(n, m)
	gen.generate_test_cases(c)
	gen.print_test_cases(c)
	if f:
		gen.print_test_cases_to_file(c, f)

def read_and_solve_case(input, method, out=None):
	parser = Parser(input)
	#opt = Optimizer([], [])
	#tester = Tester()
	solver = Solver(0, [])
	if out:
		output_file = open(out, 'w')
	for i in range(parser.c):
		solver.customers = parser.read_next_case()
		solver.length = parser.current_n
		#opt.solution = ['0' for j in range(parser.current_n)]
		solver.compute_solutions()
		sols = solver.solutions
		#opt.optimize(method)
		for s in sols:
			if s != "IMPOSSIBLE":
				solution_string = "Case #" + str(i + 1) + ": " + " ".join(s)
			else:
				solution_string = "Case #" + str(i + 1) + ": " + s
			print solution_string
			if out:
				output_file.write(solution_string)
	if out:
		output_file.close()


if __name__ == '__main__':
	# Check if the solution is provided by cmd line.

	opt_parser = argparse.ArgumentParser()

	gen_group = opt_parser.add_argument_group('Generate')

	gen_group.add_argument('-c', '--cases', dest='n_cases',
                    nargs='?', type=int, 
                    help='Number of test cases to generate.')

	gen_group.add_argument('-N', '--colors', dest='n_colors',
                    nargs='?', type=int, 
                    help='Max number of colors in the case.')

	gen_group.add_argument('-M', '--customers', dest='n_customers',
                    nargs='?', type=int, 
                    help='Max number of customers in the case')

	gen_group.add_argument('-go', '--write_case', action='store', help="The output file to write the case.")

	opt_group = opt_parser.add_argument_group('Solve and optimize')

	opt_group.add_argument("-i", "--input", help="Solve a case from a case file.")
	opt_group.add_argument("-o", "--output", help="Write solutions to a file.")
	opt_group.add_argument("-m", "--method", help="Optimization method to use",
						   choices=('random_optimizer', 'matte_minimizer'),
						   default='random_optimizer', nargs='?')

	args = opt_parser.parse_args()
	
	if args.n_cases:
		write_case(args.n_cases, args.n_colors, args.n_customers, args.write_case)

	if args.input:
		read_and_solve_case(args.input, args.method, args.output)

