# cachet-plan-recognition
Provided by: Henry Kautz (obtained from [the Cachet website](http://www.cs.rochester.edu/users/faculty/kautz/Cachet/Model_Counting_Benchmarks/index.htm)).

These are probabilistic inference queries on Bayesian networks derived from plan recognition problems.
The original formulas were weighted #SAT problems with all weights equal, and so are equivalent to unweighted formulas (all weight specifications have been removed).
For Cachet's experiments many model counting problems were derived from each formula, by assigning single variables (to compute the marginal probability with respect to that variable).

For further details see the [paper](http://www.aaai.org/Library/AAAI/2005/aaai05-075.php): Tian Sang, Paul Beame, and Henry Kautz, _Solving Bayesian Networks by Weighted Model Counting_, AAAI 2005.

Original description from the Cachet website:

_Given prior probabilities on actions and facts, the task is to compute marginal probabilities on all variables. Goals and initial conditions are observed true. Bayesian networks are generated from the plan graphs, where addional nodes (all observed false) are added to represent mutex, action-effect and preconditions of actions. Because the values of weights on variables do not affect Cachet's trace and performance, all weights are assumed to be 0.5, which is the default value and therefore is omitted in the cnf encoding. A detailed example of encoding a 4-step logistics problem is included in the archive._