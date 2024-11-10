# Copyright 2019 Xilinx Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



cd ./code1/
##SESR-S
M=7
F=16
SAVE=SESR_S_QAT

CUDA_VISIBLE_DEVICES=0 python main_qat.py --qat_step 1 --model SESR_Rep_QAT --lr 5e-4 --epochs 150 --decay 30 --data_test Set5 --save ${SAVE} --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F}  --batch_size 64 --n_GPUs 1 \

CUDA_VISIBLE_DEVICES=0 python main_qat.py --qat_step 2 --model SESR_Rep_QAT --lr 5e-4 --epochs 100 --decay 30 --data_test Set5 --save ${SAVE} --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F}  --batch_size 64 --n_GPUs 1 \

CUDA_VISIBLE_DEVICES=0 python main_qat.py --qat_step 3 --model SESR_Rep_QAT --lr 5e-4 --epochs 100 --decay 30 --data_test Set5 --save ${SAVE} --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F}  --batch_size 64 --n_GPUs 1 \

