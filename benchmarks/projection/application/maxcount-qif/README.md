# maxcount-qif
Provided by: Daniel Fremont.

These formulas are projected model counting queries made by the [MaxCount](https://github.com/dfremont/maxcount) Max#SAT solver on Quantitative Information Flow (QIF) benchmarks.
The latter, consisting of small C programs, were transformed to SAT using CBMC and then self-composed _k_ times for various values of _k_.
The first two components of the name of each formula identify the original C program (a hash table, 8-bit modular exponentiation, etc.) and the value of _k_.
The letter "s" after the value of _k_ indicates that symmetry-breaking was applied.
Finally, some formulas have a third component indicating random variants: for example _hash-8-1.cnf_ and _hash-8-2.cnf_ both derive from the basic hash table program and use _k_ = 8, but different constants were used to define the hash function.

For further details, see the [paper](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-169.html): Daniel J. Fremont, Markus N. Rabe, and Sanjit A. Seshia, _Maximum Model Counting_, AAAI 2017.

(N.B. The benchmarks in the "old" folder were previously organized as _projection/misc/misc-2_; the newer MaxCount benchmarks will be added soon.)