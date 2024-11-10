import argparse


parser = argparse.ArgumentParser(description='SESR-S for Single Image Super-Resolution')


parser.add_argument('--test_only', default='true',
                    help='set this option to test the model')
parser.add_argument('--data_range', type=str, default='1-1',
                    help='train/test data range')


args = parser.parse_args()
for arg in vars(args):
    if vars(args)[arg] == 'True':
        vars(args)[arg] = True
    elif vars(args)[arg] == 'False':
        vars(args)[arg] = False

data_range = [r.split('-') for r in args.data_range.split('/')]
if args.test_only and len(data_range) == 1:
    data_range = data_range[0]
else:
    data_range = data_range[1]

begin, end = list(map(lambda x: int(x), data_range))
print(begin, end)
