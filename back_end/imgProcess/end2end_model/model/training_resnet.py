import torch
import torch.nn as nn
from torch.autograd import Variable
import my_dataset
from resNet_model import ResNet34
import sys
from tqdm import tqdm
import numpy as np

sys.path.append('../')
# print(type(sys.path), '\r\n'.join(sys.path))

# -*- coding: UTF-8 -*-
import torch
import torch.nn as nn
from torch.autograd import Variable
import my_dataset
from cnn_model_v1 import CNN_v1
import sys
from tqdm import tqdm

# sys.path.append('../')
# print(type(sys.path), '\r\n'.join(sys.path))

import torch.nn as nn
from end2end_model.training_set_gen import gen_config

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print('using device:',DEVICE)

# Hyper Parameters
num_epochs = 30
batch_size = 300
learning_rate = 0.001 # 0.001 0.0001 0.00001
# 0.0002

def main():
    cnn = ResNet34()
    cnn.to(DEVICE)
    cnn.train()
    print('init resNet')

    criterion = nn.MultiLabelSoftMarginLoss()
    optimizer = torch.optim.Adam(cnn.parameters(), lr=learning_rate)

    lr_scheduler = torch.optim.lr_scheduler.MultiStepLR(
    optimizer, milestones=[5, 25])

    # Train the Model
    train_dataloader = my_dataset.get_train_data_loader(batch_size)
    for epoch in range(num_epochs):
        # tem_p=''
        for i, (images, labels) in tqdm(enumerate(train_dataloader)):
            images = Variable(images).to(DEVICE)
            labels = Variable(labels.float()).to(DEVICE)
            predict_labels = cnn(images)
            # print(predict_labels)
            # print(labels)
            loss = criterion(predict_labels, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # if (i+1) % 10 == 0:
            #     print("epoch:", epoch, "step:", i, "loss:", loss.item())
            # if (i+1) % 10000 == 0:
                # torch.save(cnn.state_dict(), "./model.pkl")   #current is model.pkl
                # print("save model")
                # print('epoch: %d \t batch_idx : %d \t loss: %.4f '% (epoch, i, loss))

        print("epoch:", epoch, "step:", i, "loss:", loss.item())
    torch.save(cnn.state_dict(), "./resnet_model.pkl")   #current is model.pkl
    print("save last resNet_model")

if __name__ == '__main__':
    main()