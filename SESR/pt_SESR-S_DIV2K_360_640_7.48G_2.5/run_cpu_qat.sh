##SESR-S
M=7
F=16
R='1-850/851-851'
SAVE=SESR_S_QAT
Dense_Model=../snapshot/SESR_Rep_QAT/model/model_best.pt

cd ./code1/
CUDA_VISIBLE_DEVICES=0 python test_cpu_qat.py --model SESR_Rep_QAT --scale 2 --n_resgroups ${M} --n_resblocks 1 --n_feats ${F}  --pre_train ${Dense_Model} --test_only  --data_range ${R}  --save_results