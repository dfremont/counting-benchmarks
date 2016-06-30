# cachet-deterministic-qmr
Provided by: Henry Kautz (obtained from [the Cachet website](http://www.cs.rochester.edu/users/faculty/kautz/Cachet/Model_Counting_Benchmarks/index.htm)).

_Note: for given numbers X, Y, and Z, all benchmarks with names prefixed by 'or-X-Y-Z' are simple variants of each other, differing only by unit clauses._

These are probabilistic inference queries on bipartite Bayesian networks modeling medical diagnosis problems.
The weights are chosen artificially, and the network connectivity is randomized.
For Cachet's experiments many model counting problems were derived from each formula, by assigning single variables (to compute the marginal probability with respect to that variable).

For further details see the [paper](http://www.aaai.org/Library/AAAI/2005/aaai05-075.php): Tian Sang, Paul Beame, and Henry Kautz, _Solving Bayesian Networks by Weighted Model Counting_, AAAI 2005.

Original description from the Cachet website:

_Each problem is given by a two layer bipartite network in which the top layer consists of diseases and the bottom layer consists of symptoms. If a disease may result a symptom, there is an edge from the disease to the symptom. In the CPTs for DQMR (unlike those of QMR-DT) a symptom is completely determined by the diseases that cause it; i.e., it is modeled as an OR rather than a noisy OR of its inputs. As in QMR-DT, every disease has an independent prior probability. For our experiments, we varied the numbers of diseases and symptoms from 50 to 100 and chose the edges of the bipartite graph randomly, with each symptom caused by four randomly chosen diseases. The problem was to compute the marginal probabilities for all the diseases given a set of consistent observations of symptoms. The size of the observation set varied between 10% to 30% of all symptoms._
