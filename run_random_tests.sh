#!/bin/bash
# Author jkk.lapp@gmail.com, 2015
# Usage:
#	./run_random_tests.py <n_cases_per_test> \
#		<max_colors_per_test> <max_clients_per_test>

python ./case_generator.py $1 $2 $3 > test
cat test
python ./solution_tester.py test $2

# Removing test file
rm test

