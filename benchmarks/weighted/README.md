# weighted
This folder contains weighted model counting benchmarks.

## Encoding

The benchmarks are encoded in an extension of the standard DIMACS format for CNF formulas.
Variable weights are specified with the syntax used by [Cachet](http://www.cs.rochester.edu/users/faculty/kautz/Cachet/Model_Counting_Benchmarks/index.htm):

    w 1 0.4
    w 21 -1

This indicates that variable 1 has weight 0.4, and variable 21 is unweighted (this is also the default if a weight is not specified).
Negative literals are assigned weights equal to 1 minus the corresponding positive literal weight.

Some benchmarks include comments of the following form:

    c ind 1 4 9 0
    c ind 7 42 0

The variables listed in such comments (between each `ind` and `0`) constitute an independent support of the formula, i.e., for every assignment to those variables there must be at most one extension to a complete satisfying assignment.
When an independent support is provided, all variables not in the support are unweighted.
Solvers may make use of the independent support, but need not do so, as it does not affect the weighted model count.

## Benchmark sets

* __application__
    * __cachet-deterministic-qmr__: bipartite Bayes net inference problems from Cachet
    * __cachet-grid-networks__: grid Bayes net inference problems from Cachet
