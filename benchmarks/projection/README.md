# projection
This folder contains projection counting (#∃SAT) benchmarks.

## Encoding

The benchmarks are encoded in an extension of the standard DIMACS format for CNF formulas.
The benchmarks include comments of the following form:

    c ind 1 4 9 0
    c ind 7 42 0

The variables listed in such comments (between each `ind` and `0`) comprise the projection variables of the problem: two models should be considered identical if they agree on these variables.
This is part of the problem definition, affecting the model count, and so solvers must read this information.

## Benchmark sets

* __application__
    * __pmc-symbolic-markov__: probabilistic model checking of symbolic Markov chains
* __misc__
    * __misc-1__
