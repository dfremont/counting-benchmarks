# cachet-grid-networks
Provided by: Henry Kautz (obtained from [the Cachet website](http://www.cs.rochester.edu/users/faculty/kautz/Cachet/Model_Counting_Benchmarks/index.htm)).

These are probabilistic inference queries on Bayesian networks in the form of a square grid.
The weights are chosen randomly.

For further details see the [paper](http://www.aaai.org/Library/AAAI/2005/aaai05-075.php): Tian Sang, Paul Beame, and Henry Kautz, _Solving Bayesian Networks by Weighted Model Counting_, AAAI 2005.

Original description from the Cachet website:

_A grid network is an N x N grid, where there are two directed edges from a node to its neighbors right and down. The upper-left node is a source, and the bottom-right node is a sink. The query is to compute the probability of the sink being true given no evidence. The deterministic ratio is a parameter specifying the fraction of nodes that are deterministic, that is, whose values are determined given the values of their parents. There are 10 random instances generated for each size._
