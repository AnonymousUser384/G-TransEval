# G-TransEval
This artifact for our paper "On the Evaluation of Neural Code Translation: Taxonomy and Benchmark" includes benchmark suite, results, materials and source code of our automatic unit test tool. We hope this artifact can motivate and help future research on code translation. 

What's inside the artifact:

1. A benchmark suite of 400 code translation pairs between 5 languages, i.e., Python, C++, Java, C#, and JavaScript (Section V). Located in ./G-TransEval
2. Empirical study material (Section II and III). Located in ./EmpiricalStudy
3. Taxonomy examples and experiment results (Section IV). Located in ./Taxonomy
4. Our automatic unit test tool for G-TransEval. Located in ./TestRunner

## Taxonomy
We develop a taxonomy that categorizes code translation tasks into four primary types according to their complexity and knowledge dependence: 
- Token Level (Type 1): Map trivial tokens to their equivalent in the target
- Syntactic Level (Type 2): Migrate syntactic structures based on linguistic rules
- Library Level (Type 3): Migrate library to their equivalent in the target language
- Algorithm Level (Type 4): Reimplement the program in the target language using a different algorithm

## Unit Test Runner
The automatic unit test tool is placed in the `TestRunner` folder. See [detailed instruction](TestRunner/README.md) for usages. 



