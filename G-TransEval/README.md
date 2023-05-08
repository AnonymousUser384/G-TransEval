## G-TransEval
G-TransEval is the first categorized test set designed to provide fine-grained and extensive evaluations of code translation models. Our benchmark leverages existing benchmarks and extends them to involve all four translation types. To increase the reliability of performance measures, Each test sample are augmented with unit test cases.

G-TransEval comprises a total of 400 code translation pairs between 5 languages, i.e., Python, C++, Java, C#, and JavaScript. The first three types consis of 125 translation pairs each, and the fourth type compries 25 translation pairs. Our dataset are available at [G-TransEval](/G-TransEval). The folder structure is as follows:

- Test_all: The test data across all four types
- Type 1: Token level translation
- Type 2: Syntax level translation
- Type 3: Library level translation
- Type 4: Algorithm level translation
