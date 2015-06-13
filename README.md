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
