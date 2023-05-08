# BenchmarkResults
Here lists the results of different models on our benchmark.

## Translation Results
The translations of CodeT5, TransCoder and TransCoder-ST are listed in the `translation_results` folder. Their results of unit tests are listed in the `unit_test_results` folder.

Moreover, we explore the results of training CodeT5 with only 1000, 500, 200 and 100 samples. Here displays the full data of the experiment that explores the impact of size of training samples in our paper.

|            | Target               | Java→X |      |        |      |        |      |        |    | X→Java |      |        |      |        |      |        |    |
|------------|----------------------|--------|------|--------|------|--------|------|--------|----|--------|------|--------|------|--------|------|--------|----|
| Source     | Type                 | Type 1 |      | Type 2 |      | Type 3 |      | Type 4 |    | Type 1 |      | Type 2 |      | Type 3 |      | Type 4 |    |
|            | Train Size \ Metrics | BLEU   | CA   | BLEU   | CA   | BLEU   | CA   | BLEU   | CA | BLEU   | CA   | BLEU   | CA   | BLEU   | CA   | BLEU   | CA |
| C++        | 100                  | 96.59  | 79.2 | 82.54  | 21.6 | 69.72  | 3.2  | 28.22  | 0  | 95.94  | 79.2 | 68.25  | 24   | 59.2   | 8.8  | 23.92  | 0  |
|            | 200                  | 96.5   | 88   | 86.25  | 40.8 | 74.13  | 11.2 | 27.71  | 0  | 96.85  | 88   | 75.55  | 39.2 | 66.17  | 16   | 28.88  | 0  |
|            | 500                  | 96.15  | 88   | 88.97  | 55.2 | 76.03  | 18.4 | 31.12  | 0  | 96.41  | 88.8 | 79.01  | 50.4 | 71.18  | 19.2 | 32.35  | 0  |
|            | 1000                 | 95.63  | 94.4 | 91.28  | 64.8 | 78.8   | 27.2 | 34.65  | 0  | 97.18  | 90.4 | 80.67  | 66.4 | 72.62  | 29.6 | 32.06  | 0  |
|            | Full                 | 94.14  | 90.4 | 91.33  | 72.8 | 83.66  | 48   | 31.76  | 0  | 97.39  | 94.4 | 82.15  | 83.2 | 74.52  | 58.4 | 33.8   | 0  |
| Python     | 100                  | 80.15  | 56.8 | 70.48  | 20.8 | 67.11  | 4    | 36.86  | 0  | 77.01  | 44   | 53.07  | 7.2  | 49.57  | 4    | 15.79  | 0  |
|            | 200                  | 82.44  | 63.2 | 75.57  | 38.4 | 70.44  | 8.8  | 39.35  | 0  | 80.27  | 56   | 59.29  | 13.6 | 56.43  | 4.8  | 18.32  | 0  |
|            | 500                  | 83.18  | 72.8 | 78.83  | 52.8 | 74.52  | 17.6 | 35.59  | 0  | 80.05  | 60   | 62.88  | 24.8 | 61.58  | 8.8  | 20.77  | 0  |
|            | 1000                 | 83.33  | 80   | 80.27  | 63.2 | 78.54  | 31.2 | 38.89  | 0  | 80.15  | 63.2 | 65.92  | 30.4 | 63.18  | 16.8 | 22.27  | 0  |
|            | Full                 | 82.71  | 88   | 78.9   | 74.4 | 78.62  | 68   | 37.08  | 0  | 81.98  | 78.4 | 69.57  | 50.4 | 67.47  | 44.8 | 21.79  | 0  |
| C#         | 100                  | 98.03  | 90.4 | 91.43  | 40   | 82.8   | 17.6 | 49.44  | 0  | 97.52  | 88.8 | 78.41  | 27.2 | 71.36  | 9.6  | 34.86  | 0  |
|            | 200                  | 98.54  | 94.4 | 92.8   | 45.6 | 83.73  | 17.6 | 59.65  | 0  | 98.45  | 93.6 | 83.24  | 47.2 | 77.04  | 17.6 | 52.43  | 0  |
|            | 500                  | 98.92  | 96.8 | 95.65  | 69.6 | 88.5   | 32   | 60.38  | 0  | 98.17  | 91.2 | 92.89  | 59.2 | 82.94  | 24   | 54.1   | 0  |
|            | 1000                 | 99.09  | 96   | 95.56  | 73.6 | 88.13  | 42.4 | 64.41  | 0  | 98.81  | 96.8 | 95.39  | 71.2 | 86.55  | 29.6 | 51.59  | 0  |
|            | Full                 | 98.38  | 92.8 | 93.58  | 77.6 | 85.62  | 66.4 | 58.86  | 0  | 98.59  | 97.6 | 94.75  | 75.2 | 87.48  | 56.8 | 55.8   | 0  |
| JavaScript | 100                  | 83.59  | 68   | 75.55  | 26.4 | 68.06  | 6.4  | 42.72  | 0  | 91.4   | 60.8 | 66.36  | 13.6 | 61.82  | 2.4  | 23.66  | 0  |
|            | 200                  | 85.56  | 75.2 | 81.96  | 51.2 | 73.25  | 13.6 | 43.86  | 0  | 92.44  | 68.8 | 68.03  | 25.6 | 65.97  | 6.4  | 27.85  | 0  |
|            | 500                  | 85.05  | 72.8 | 83.52  | 57.6 | 74.95  | 23.2 | 40.41  | 0  | 92.85  | 71.2 | 75.48  | 40   | 72.03  | 16   | 34.78  | 0  |
|            | 1000                 | 86.02  | 81.6 | 84.67  | 68.8 | 76.15  | 33.6 | 44.59  | 0  | 93.56  | 75.2 | 75.2   | 44.8 | 71.83  | 20   | 27.8   | 0  |
|            | Full                 | 84.67  | 85.6 | 82.74  | 73.6 | 75.18  | 52.8 | 43.2   | 8  | 93.46  | 76.8 | 80.35  | 62.4 | 74.26  | 37.6 | 29.71  | 0  |