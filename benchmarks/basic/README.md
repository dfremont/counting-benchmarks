# basic
This folder contains model counting (#SAT) benchmarks.

## Encoding

The benchmarks are encoded in an extension of the standard DIMACS format for CNF formulas.
Some benchmarks include comments of the following form:

    c ind 1 4 9 0
    c ind 7 42 0

The variables listed in such comments (between each `ind` and `0`) constitute an independent support of the formula, i.e., for every assignment to those variables there must be at most one extension to a complete satisfying assignment.
Solvers may make use of this information, but need not do so, as it does not affect the model count.

## Benchmark sets

* __application__
    * __cachet-plan-recognition__: unweighted Bayes net inference problems from Cachet
* __quasi-application__
    * __iscas89-xor__: ISCAS'89 circuits with random XOR clauses