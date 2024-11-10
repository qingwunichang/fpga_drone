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

import torch

import utility
import data
import model
import loss
from option import args
from trainer import Trainer
#from ptflops import get_model_complexity_info

torch.manual_seed(args.seed)
checkpoint = utility.checkpoint(args)


def parse_model(model):
    from pytorch_nndct import Pruner
    from nndct_shared.utils import saving

    inputs = torch.randn([1, 3, 360, 640], dtype=torch.float32).cuda()
    pruner = Pruner(model, inputs)
    graph = pruner._graph
    graph_name = graph.name
    saving.save_graph(graph,
           json_path='{}_config.json'.format(graph_name),
           hdf5_path='{}.hdf5'.format(graph_name))


def get_model_flops(model_name, model, input_W, input_H):
    from torchprofiler import Profiler

    # Initialize your profiler
    profiler = Profiler(model)

    # Run for specified input shape
    profiler.run((1,3,input_H, input_W)) # Include batch_size. e.g. (1, 3, 224, 224)

    # Print summary
    profiler.print_summary()

    # You can also view the overall statistics respectively
    profiler.total_input
    profiler.total_output
    profiler.total_params
    profiler.total_flops
    profiler.trainable_params

    print('Model name:', model_name)



def main():
    global model
    if args.data_test == ['video']:
        from videotester import VideoTester
        model = model.Model(args, checkpoint)
        t = VideoTester(args, model, checkpoint)
        t.test()
    else:
        if checkpoint.ok:
            loader = data.Data(args)
            model = model.Model(args, checkpoint)
            #macs, params = get_model_complexity_info(model, (3, 360, 640), as_strings=True,
            #                               print_per_layer_stat=True, verbose=True)
            #print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
            #print('{:<30}  {:<8}'.format('Number of parameters: ', params))
            _loss = loss.Loss(args, checkpoint) if not args.test_only else None
            t = Trainer(args, loader, model, _loss, checkpoint)
            while not t.terminate():
                t.train()
                t.test()
            checkpoint.done()

if __name__ == '__main__':
    main()
