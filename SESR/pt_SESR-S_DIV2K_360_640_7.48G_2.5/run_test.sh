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
###SESR-S model
Dense_Model=../float/SESR_S/model/model_best.pt
Rep_Model=../float/SESR_S/model/model_best_rep.pt
##config
M=7
F=16

#evaluation dense mode
CUDA_VISIBLE_DEVICES=0 python main.py --model SESR --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F} --data_test Set5+Set14+B100+Urban100  --pre_train ${Dense_Model} --test_only 

#re-parameter 
CUDA_VISIBLE_DEVICES=7 python convert.py --model SESR --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F} --trained_model ${Dense_Model} --deployed_model ${Rep_Model}

#evaluation rep model
CUDA_VISIBLE_DEVICES=0 python main.py --model SESR_Rep --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F} --data_test Set5+Set14+B100+Urban100 --pre_train ${Rep_Model} --test_only --deploy 
