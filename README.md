# paintshop
Paintshop problem solver.

## Usage

Every module has its own test module.

To generate cases and solve them, use main.py module:

`python ./main.py <C> <MAX_N> <MAX_M> [METHOD]`

Arguments:

* C: Integer for the number of cases to generate.
* MAX_N: Max number of colors for the cases. The length of the solution will be exactly MAX_N.
* MAX_M: Max number of customers in each of the case generated.
* METHOD: Optional. One of the built-in optimization methods provided. A random method will be used if not provided.
	* matte_minimizer.
	* targeted_color.

If you want to know more about optimization methods, read the Optimization methods section.

Note: There are known issues if MAX_N and MAX_M are too big ~ 50 or more.

## Methods

### Matte minimizer

This strategy generates a 'naive optimal solution', this is, a batch with all colors in glossy variety. Then, it switches from glossy to matte one by one and checks if the solution satisfies. If it does, stops the optimization.

### Random minimizer

This method randomly switches 1s by 0s and viceversa.

### Method discussion

Given the complexity of this SAT problem, I chose to use random methods to try and provide solutions.
The matte_minimizer is a good strategy to try and optimize a valid solution but
If the length of the solution is not very big however, I would use the random method.

### Examples and performance 

```
python ./main.py -c 1 -N 10 -M 10 -go test_file
1
9
5
6 3 0 9 1 7 0 2 0 6 0 5 0
6 7 0 5 1 1 0 2 0 3 0 4 0
8 8 0 7 1 4 0 1 0 3 0 5 0 9 0 2 0
2 8 1 1 0
4 7 0 6 0 1 1 5 0
```

Run some tests using cProfile profiler to get execution time.

```
python -m cProfile ./main.py -i test_file -m random_optimizer
Case #1: 0 0 0 0 0 0 0 0 0
         26615 function calls (26583 primitive calls) in 0.054 seconds

```

Using the matte minimizer method:

```
python -m cProfile ./main.py -i test_file -m matte_minimizer
Case #1: 0 0 0 0 0 0 0 0 0
         26615 function calls (26583 primitive calls) in 0.057 seconds
```