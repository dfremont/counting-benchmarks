# counting-benchmarks
A collection of model counting (#SAT) benchmarks.
If you have some interesting instances, please consider submitting them! See below for details.

This repository lives at [http://tinyurl.com/countingbenchmarks](http://tinyurl.com/countingbenchmarks).

## Organization

All the benchmarks are contained in the __benchmarks__ folder, which has three subfolders for different types of problems:

* __basic__: #SAT problems
* __projection__: projection counting (#∃SAT) problems
* __weighted__: weighted #SAT problems

Each of these problem types is in turn divided into several categories:

* __application__: instances arising from applications
* __quasi-application__: instances derived from SAT instances that arise from applications (e.g. taking an industrial SAT instance and treating it as a #SAT instance even if the model count isn't necessarily meaningful)
* __crafted__: specially constructed instances not necessarily having an application
* __random__: randomly generated instances
* __misc__: instances that have not been categorized

Within these categories are folders for each set of benchmarks.
Each set has a _README_ file explaining how the benchmarks were generated and citing any relevant papers.
The __misc__ benchmarks may include sets lacking a description, e.g. if they derive from work that has not yet been published.

For convenience in running experiments with all benchmarks of a given type, every folder contains a _benchmarkList.txt_ file listing paths to every benchmark in the folder.
For example, one can use the list in __projection/application/pmc-symbolic-markov__ to run all the benchmarks from that particular set, or the list in __projection__ to run all projection counting benchmarks from any set.
Occasionally a benchmark set includes the same benchmark in multiple different subfolders; the _benchmarkList.txt_ files will only list the benchmark once.

## Encodings

All three types of benchmarks are encoded in extensions of the standard DIMACS format for CNF formulas.
The _README_ files in the __basic__, __projection__, and __weighted__ folders explain the extension used for the corresponding type of benchmark.
All benchmarks have been compressed with _gzip_.

## Submitting Benchmarks

We are trying to put together a wide variety of benchmarks from as many sources as possible.
If you would like to submit some new instances, [contact me](https://math.berkeley.edu/~dfremont/contact.html) (but please don't attach large benchmarks to an email).
Remember to include a description of how the instances were generated.
Thank you for contributing!
