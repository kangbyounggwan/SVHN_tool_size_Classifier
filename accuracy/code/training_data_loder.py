import torch
import torch.nn.init
import torchvision.datasets as dsets
import torchvision.transforms as transforms
import torch.nn as nn
import torchvision
from torch.utils.data import DataLoader
import wandb
import os

os.environ['WANDB_NOTEBOOK_NAME'] = 'some text here'
wandb.init(project="my-costom")

learning_rate = 1e-5
epoch = 100
batch_size = 10

trans = transforms.Compose([

    transforms.ToTensor()
])

train_data = torchvision.datasets.ImageFolder(root='desktop/data', transform=trans)

trans = transforms.Compose([

    transforms.Resize((64, 128)),
    transforms.ToTensor()
])

test_data = torchvision.datasets.ImageFolder(root='desktop/data', transform=trans)

train_loader = DataLoader(dataset = train_data,batch_size=4,shuffle=True, num_workers=2)
test_loader  = DataLoader(dataset=test_data, batch_size = len(test_data))