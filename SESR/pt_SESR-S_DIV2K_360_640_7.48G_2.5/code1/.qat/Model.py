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

# GENETARED BY NNDCT, DO NOT EDIT!

import torch
import pytorch_nndct as py_nndct
class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.module_0 = py_nndct.nn.Input() #Model::input_0
        self.module_1 = py_nndct.nn.quant_input() #Model::Model/QuantStub[model]/QuantStub[quant_stub]/input.1
        self.module_2 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/MeanShiftConv[model]/MeanShiftConv[sub_mean]/Conv2d[mean_conv]/input.2
        self.module_3 = py_nndct.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], groups=1, bias=False) #Model::Model/ConvGroup[model]/ConvGroup[head]/Conv2d[body_reparam]/input.3
        self.module_4 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[0]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1308
        self.module_5 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[0]/input.4
        self.module_6 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[0]/ReLU[act]/input.5
        self.module_7 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[1]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1331
        self.module_8 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[1]/input.6
        self.module_9 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[1]/ReLU[act]/input.7
        self.module_10 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[2]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1354
        self.module_11 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[2]/input.8
        self.module_12 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[2]/ReLU[act]/input.9
        self.module_13 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[3]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1377
        self.module_14 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[3]/input.10
        self.module_15 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[3]/ReLU[act]/input.11
        self.module_16 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[4]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1400
        self.module_17 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[4]/input.12
        self.module_18 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[4]/ReLU[act]/input.13
        self.module_19 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[5]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1423
        self.module_20 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[5]/input.14
        self.module_21 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[5]/ReLU[act]/input.15
        self.module_22 = py_nndct.nn.Conv2d(in_channels=16, out_channels=16, kernel_size=[3, 3], stride=[1, 1], padding=[1, 1], dilation=[1, 1], groups=1, bias=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[6]/Sequential[body]/RCAB[0]/Conv2d[body_reparam]/1446
        self.module_23 = py_nndct.nn.Add() #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[6]/input.16
        self.module_24 = py_nndct.nn.ReLU(inplace=False) #Model::Model/Sequential[model]/Sequential[body]/ResidualGroup[6]/ReLU[act]/1449
        self.module_25 = py_nndct.nn.Add() #Model::Model/Add[model]/Add[skip_add]/input.17
        self.module_26 = py_nndct.nn.Conv2d(in_channels=16, out_channels=12, kernel_size=[5, 5], stride=[1, 1], padding=[2, 2], dilation=[1, 1], groups=1, bias=False) #Model::Model/ConvGroup[model]/ConvGroup[tail]/Conv2d[body_reparam]/1471
        self.module_27 = py_nndct.nn.Module('pixel_shuffle',upscale_factor=2) #Model::Model/PixelShuffle[model]/PixelShuffle[ps]/input
        self.module_28 = py_nndct.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=[1, 1], stride=[1, 1], padding=[0, 0], dilation=[1, 1], groups=1, bias=True) #Model::Model/MeanShiftConv[model]/MeanShiftConv[add_mean]/Conv2d[mean_conv]/1492
        self.module_29 = py_nndct.nn.dequant_output() #Model::Model/DeQuantStub[model]/DeQuantStub[dequant_stub]/1493

    def forward(self, *args):
        output_module_0 = self.module_0(input=args[0])
        output_module_0 = self.module_1(input=output_module_0)
        output_module_0 = self.module_2(output_module_0)
        output_module_0 = self.module_3(output_module_0)
        output_module_4 = self.module_4(output_module_0)
        output_module_4 = self.module_5(other=output_module_0, alpha=1, input=output_module_4)
        output_module_4 = self.module_6(output_module_4)
        output_module_7 = self.module_7(output_module_4)
        output_module_7 = self.module_8(other=output_module_4, alpha=1, input=output_module_7)
        output_module_7 = self.module_9(output_module_7)
        output_module_10 = self.module_10(output_module_7)
        output_module_10 = self.module_11(other=output_module_7, alpha=1, input=output_module_10)
        output_module_10 = self.module_12(output_module_10)
        output_module_13 = self.module_13(output_module_10)
        output_module_13 = self.module_14(other=output_module_10, alpha=1, input=output_module_13)
        output_module_13 = self.module_15(output_module_13)
        output_module_16 = self.module_16(output_module_13)
        output_module_16 = self.module_17(other=output_module_13, alpha=1, input=output_module_16)
        output_module_16 = self.module_18(output_module_16)
        output_module_19 = self.module_19(output_module_16)
        output_module_19 = self.module_20(other=output_module_16, alpha=1, input=output_module_19)
        output_module_19 = self.module_21(output_module_19)
        output_module_22 = self.module_22(output_module_19)
        output_module_22 = self.module_23(other=output_module_19, alpha=1, input=output_module_22)
        output_module_22 = self.module_24(output_module_22)
        output_module_22 = self.module_25(other=output_module_0, alpha=1, input=output_module_22)
        output_module_22 = self.module_26(output_module_22)
        output_module_22 = self.module_27(output_module_22)
        output_module_22 = self.module_28(output_module_22)
        output_module_22 = self.module_29(input=output_module_22)
        return output_module_22
