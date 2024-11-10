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



##SESR-S
M=7
F=16
SAVE=SESR_S

cd ./code1/
CUDA_VISIBLE_DEVICES=0 python main.py --model SESR --lr 5e-4 --save ${SAVE} --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F}  --batch_size 32 --n_GPUs 1
