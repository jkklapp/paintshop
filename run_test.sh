#!/bin/bash
# Author jkk.lapp@gmail.com, 2015
# Usage:
#	./run_test.sh <n_cases_per_test> \ 
#		<max_colors_per_test> <max_clients_per_test> \
#		<solution>
#
# All arguments are integers except solution
# which is a string like "0 0 0 1" containing a
# solution

if [ "$#" -ne 4 ]; then
	echo "usage: ./run_test.sh <n_cases_per_test> <max_colors_per_test> max_clients_per_test> <solution>"
	exit 0
fi

python ./case_generator.py $1 $2 $3 > test
cat test
python ./solution_tester.py test $2 $4

# Removing test file
rm test

