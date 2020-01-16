# symbolic-sygus
Provided by: Daniel Fremont (with thanks to Garvit Juniwal and Kuldeep Meel).

These formulas are synthesis queries made by the symbolic Syntax-Guided Synthesis (SyGuS) solver by Garvit Juniwal on the "Hacker's Delight" SyGuS benchmarks (which can be found on the [SyGuS website](https://sygus.org/)).
For each benchmark, e.g. "hd-04-d0-prog", there is a series of formulas corresponding to each iteration of the CEGIS loop: for example, "hd-04-d0-prog_2.cnf" is the second synthesis query made by the solver.
The projection variables parametrize the space of programs being searched over, so that the projected model count of each formula counts programs which are correct on the counterexamples seen so far during CEGIS.

We have organized the formulas into two folders based on the difficulty level "d0" or "d1", corresponding to the SyGuS grammar used.
Note that some of the Hacker's Delight benchmarks cannot be solved at all by the symbolic SyGuS solver in a reasonable time; since model counting is harder than satisfiability checking, we have omitted those benchmarks here.
In particular there is no "d5" folder, since the symbolic SyGuS solver cannot solve any of the benchmarks using the "d5" grammar.


For details about the construction of these formulas, see the SyGuS [paper](https://doi.org/10.1109/FMCAD.2013.6679385): Rajeev Alur, Rastislav Bodik, Garvit Juniwal, Milo M. K. Martin, Mukund Raghothaman, Sanjit A. Seshia, Rishabh Singh, Armando Solar-Lezama, Emina Torlak, and Abhishek Udupa, _Syntax-Guided Synthesis_, FMCAD 2013.

(N.B. This benchmark set was previously organized under _projection/misc/misc-1_)