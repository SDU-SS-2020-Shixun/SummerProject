# -*- coding: UTF-8 -*-
import sys
import os
from torch.utils.data import DataLoader,Dataset
import torchvision.transforms as transforms
from PIL import Image

sys.path.append('../')
# print(type(sys.path), '\r\n'.join(sys.path))

import torch.nn as nn
from end2end_model.training_set_gen import gen_config
from end2end_model.training_set_gen import one_hot_encoding as ohe

class mydataset(Dataset):

    def __init__(self, folder, transform=None):
        self.train_image_file_paths = [os.path.join(folder, image_file) for image_file in os.listdir(folder)]
        self.transform = transform

    def __len__(self):
        return len(self.train_image_file_paths)

    def __getitem__(self, idx):
        image_root = self.train_image_file_paths[idx]
        image_name = image_root.split(os.path.sep)[-1]
        image = Image.open(image_root)
        if self.transform is not None:
            image = self.transform(image)
        # print('DUBUG IN MY_DATASET:',image_name.split('_')[0])
        label = ohe.encode(image_name.split('_')[0]) # 为了方便，在生成图片的时候，图片文件的命名格式 "4个数字或者数字_时间戳.PNG", 4个字母或者即是图片的验证码的值，字母大写,同时对该值做 one-hot 处理
        return image, label

transform = transforms.Compose([
    # transforms.ColorJitter(),
    transforms.Grayscale(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
def get_train_data_loader(BATCH_SIZE=64):

    dataset = mydataset(gen_config.TRAIN_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

def get_test_data_loader():
    dataset = mydataset(gen_config.TEST_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)
    

def get_predict_data_loader():
    dataset = mydataset(gen_config.PREDICT_DATASET_PATH, transform=transform)
    return DataLoader(dataset, batch_size=1, shuffle=True)