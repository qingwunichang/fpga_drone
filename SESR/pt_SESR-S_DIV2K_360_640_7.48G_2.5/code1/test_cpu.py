import torch
from importlib import import_module
import utility
from tester import Trainer
import data
import model
from tqdm import tqdm
import loss
from option import args
from torch.utils.data import DataLoader, Dataset
import os

torch.manual_seed(args.seed)
checkpoint = utility.checkpoint(args)

class SimpleDataset(Dataset):
    def __init__(self, hr_images, lr_images):
        self.hr_images = hr_images
        self.lr_images = lr_images

    def __len__(self):
        return len(self.hr_images)

    def __getitem__(self, idx):
        hr_image = torch.load(self.hr_images[idx])
        lr_image = torch.load(self.lr_images[idx])
        return lr_image, hr_image

class Data:
    def __init__(self, args):
        self.loader_test = []
        self.dir_hr = "../data/DIV2K/bin/DIV2K_train_HR"
        self.dir_lr = "../DIV2K_train_LR_bicubic/X2"
        self.num_images = list(map(int, args.range.split("-")))
        self.hr_images, self.lr_images = self._scan()

        # 创建测试集
        testset = SimpleDataset(self.hr_images, self.lr_images)

        # 定义 DataLoader
        self.loader_test.append(
            DataLoader(
                testset,
                batch_size=1,
                shuffle=False,
                pin_memory=not args.cpu,
            )
        )

    def _scan(self):
        hr_images = sorted([os.path.join(self.dir_hr, f) for f in os.listdir(self.dir_hr) if f.endswith('.pt')])
        lr_images = sorted([os.path.join(self.dir_lr, f) for f in os.listdir(self.dir_lr) if f.endswith('.pt')])

        # 根据指定范围裁剪图像列表
        if self.num_images:
            hr_images = hr_images[self.num_images[0]:self.num_images[1]]
            lr_images = lr_images[self.num_images[0]:self.num_images[1]]

        return hr_images, lr_images

model = model.Model(args, checkpoint)
loader = Data(args)
_loss = loss.Loss(args, checkpoint) if not args.test_only else None
t = Trainer(args, loader, model, _loss, checkpoint)
t.test()


