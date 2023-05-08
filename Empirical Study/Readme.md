# Empirical Study
Here lists the results of RQ1 and RQ2 in our paper.

### RQ1

A fine-grained manual evaluation was conducted on 100 samples with unit tests from TransCoder-test dataset. The generated results of models are placed in [`rq1`](./rq1) folder. The results show that the models are most likely to make mistakes on API, followed by Syntactic Structure. Supervised approaches are more likely to make mistakes on Symbol.

| Task:<br>Java→C++            | CodeBERT | CodeT5 | TransCoder | TransCoder-ST |
|---------------------|----------|--------|------------|---------------|
| Semantic            | 67       | 80     | 75         | 79            |
| API                 | 86       | 92     | 82         | 85            |
| Syntactic Structure | 89       | 96     | 95         | 100           |
| Keyword             | 94       | 98     | 97         | 99            |
| Identifier          | 99       | 99     | 100        | 100           |
| Symbol              | 90       | 94     | 100        | 99            |

### RQ2

The BLEU and EM scores of CodeT5 on exisiting benchmarks are displayed here. We found that current datasets contain too many simple and naive translation pairs, leading to very high BLEU and EM scores. The generated results of models are placed in [`rq2`](./rq2) folder.

| Model:<br>CodeT5 | Task\Metric | BLEU  | EM    |
|------------------|-------------|-------|-------|
| CodeXGLUE        | Java→C#     | 91.46 | 68.1  |
|                  | C#→ Java    | 92.42 | 72.6  |
| TransCoder-test  | Java→C++    | 90.47 | 32.17 |
|                  | C++→ Java   | 90.25 | 37.03 |
| XLCoST-m         | Java→C++    | 93.48 | 51.1  |
|                  | C++→ Java   | 93.29 | 51.2  |

### Taxonomy

Here's complete results of experiment performed on catagorized TransCoder-test benchmark that we omitted in out paper.

| Full Dataset  | BLEU  | CodeBLEU | EM    | CA    |
|---------------|-------|----------|-------|-------|
| Naive Copy    | 78.39 | 79.96    | 1.05  | 29.55 |
| CodeBERT      | 87.95 | 86.79    | 23.42 | 72.59 |
| CodeT5        | 90.47 | 90.00    | 32.17 | 82.23 |
| TransCoder    | 84.23 | 85.00    | 16.03 | 80.30 |
| TransCoder-ST | 83.95 | 84.90    | 16.77 | 84.37 |

| Type-1        | BLEU  | CodeBLEU | EM    | CA    |
|---------------|-------|----------|-------|-------|
| Naive Copy    | 90.47 | 89.68    | 2.60  | 52.43 |
| CodeBERT      | 92.96 | 91.42    | 38.28 | 83.98 |
| CodeT5        | 95.80 | 94.73    | 48.44 | 91.75 |
| TransCoder    | 92.04 | 91.51    | 29.43 | 93.20 |
| TransCoder-ST | 91.92 | 91.30    | 31.51 | 94.17 |

| Type-2        | BLEU  | CodeBLEU | EM    | CA    |
|---------------|-------|----------|-------|-------|
| Naive Copy    | 76.22 | 76.97    | 0.00  | 15.29 |
| CodeBERT      | 86.74 | 85.64    | 17.30 | 67.65 |
| CodeT5        | 88.90 | 88.31    | 25.22 | 75.29 |
| TransCoder    | 83.54 | 83.63    | 10.56 | 79.41 |
| TransCoder-ST | 83.06 | 83.25    | 9.68  | 85.29 |

| Type-3        | BLEU  | CodeBLEU | EM    | CA    |
|---------------|-------|----------|-------|-------|
| Naive Copy    | 60.92 | 67.80    | 0.00  | 4.4   |
| CodeBERT      | 81.18 | 80.62    | 7.17  | 56.04 |
| CodeT5        | 83.67 | 84.42    | 14.80 | 73.63 |
| TransCoder    | 71.82 | 75.94    | 1.35  | 52.75 |
| TransCoder-ST | 71.56 | 76.36    | 2.24  | 60.44 |
