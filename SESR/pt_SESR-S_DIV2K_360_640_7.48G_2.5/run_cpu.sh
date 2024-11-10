##SESR-S
M=7
F=16
R='0-100'
SAVE=SESR_S
Dense_Model=../snapshot/SESR_S/model/model_best.pt

cd ./code1/
CUDA_VISIBLE_DEVICES=0 python test_cpu.py --model SESR --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F}  --pre_train ${Dense_Model} --test_only  --data_range ${R}  --save_results