# SESR: Single Image Super Resolution with Recursive Squeeze and Excitation Networks

## Contents

1. [Environment](#Environment)
2. [Preparation](#Preparation)
3. [Evaluation/Training/Quantization](#Evaluation/Training/Quantization)
4. [Performance](#Performance)
5. [Model_info](#Model info)

## Environment
1. Environment requirement
  - python 3.7, pytorch, pillow, numpy 1.15.0...

2. Installation
   - Create virtual envrionment and activate it (without docker):
   ```shell
   conda create -n torch-1.7 python=3.7
   conda activate torch-1.7
   ```
   - Activate virtual envrionment (with docker):
   ```shell
   conda vitis-ai-pytorch
   ```
   - Install all the python dependencies using pip:
   ```shell
   pip install --user -r requirements.txt
   ```
Note: If you are in the released Docker env, there is no need to create virtual envrionment.
## Preparation

1. Datasets description
   - [DIV2K](https://data.vision.ee.ethz.ch/cvl/DIV2K/)
   - [Benchmarks](https://cv.snu.ac.kr/research/EDSR/benchmark.tar)
 
2. Dataset structure
   ```
   + data
       + DIV2K
       + benchmark
   ```
## Evaluation/Training/Quantization

1. Model description
   SESR with small parameters (SESR-S) for scale=2x. 

2. Evaluation
   ```
   # perform evaluation on 4 benchmarks: Set5, Set14, B100, Urabn100
   sh run_test.sh
   ```
3. Training
   ```
   # perform training on DIV2K dataset
   sh run_train.sh
   ```
4. Quantization-Qware Training (QAT)
   ```
   # perform qat on DIV2K dataset
   sh run_qat.sh
   ```

## Performance

| Method     | Scale | Flops | Set5         |  Set14        | B100 | Urban100 |
|------------|-------|-------|--------------|---------------|----------|-------|
|Bicubic     |X2     | - | 33.66 / 0.9299|30.24 / 0.8688|29.56 / 0.8431|26.88 / 0.8403|
|SESR-S (float) |X2 |7.48G |37.309 / 0.958|32.894 / 0.911|31.663 / 0.893|30.276 / 0.908|
|SESR-S (INT8) |X2  |7.48G |36.813 / 0.95|32.607 / 0.906|31.443 / 0.889|29.901 / 0.899|
- Note: the Flops is calculated with the output resolution is 720x1280

## Model_info

1. Data preprocess
  ```
  data channel order: BGR(0~255)                  
  input = input 
  ```
2. System Environment

The operation and accuracy provided above are verified in Ubuntu16.04.10, cuda-9.0, Driver Version: 460.32.03, GPU NVDIA P100




