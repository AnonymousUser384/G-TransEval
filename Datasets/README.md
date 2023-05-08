# Datasets a
Here lists other datasets used in our paper.

## Datasets 

### CodeXGLUE
Data of code translation subtask in [CodeXGLUE](https://microsoft.github.io/CodeXGLUE/) benchmark. All the code data are tokenized to achieve consistency on calculation method of BLEU and CodeBLEU.

### XLCoST-m
Data of method level code translation extracted from [XLCoST](https://github.com/reddy-lab-code-research/XLCoST), which only support snippet and program level code translation originally. The train set of XLCoST-m is used for training CodeBERT and CodeT5 on TransCoder-test and G-TransEval benchmarks.

### TransCoder-test
The test dataset of [TransCoder](https://github.com/facebookresearch/CodeGen/tree/main/data/test_dataset). For Java-C++ translations, we catagorize the test set into three levels, placed in `transcoder-test-catagorized` folder.

