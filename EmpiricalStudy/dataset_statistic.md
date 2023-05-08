# Datasets
Here lists other datasets used in our paper.

## Datasets 

### CodeXGLUE
Data of code translation subtask in [CodeXGLUE](https://microsoft.github.io/CodeXGLUE/) benchmark. All the code data are tokenized to achieve consistency on calculation method of BLEU and CodeBLEU.

### XLCoST-m
`Method level paralle dataset` extracted from [XLCoST](https://github.com/reddy-lab-code-research/XLCoST), which only supports snippet and program level code translation originally. The train set of XLCoST-m is used for training supervised model CodeBERT and CodeT5.

### TransCoder-test
The test dataset of [TransCoder](https://github.com/facebookresearch/CodeGen/tree/main/data/test_dataset). For Java-C++ translations, we catagorize the test set into three levels, placed in `transcoder-test-catagorized` folder.

### Statistics
|Datasets|Train |Valid|Test |Languages|
|---|:-:|:-:|:-:|:-:|
|CodeXGLUE|10,253|499  |1,000|Java, C#|
|XLCoST-m|8,389 |500  |1,000|Java, C++, Python, C#, JavaScript|
|TransCoder-test|- |470  |948|Java, C++, Python|
