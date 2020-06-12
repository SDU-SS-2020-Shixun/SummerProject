import torch
import torch.nn as nn
import sys
import os

# 修改导入路径
sys.path.append('../back_end/imgProcess/end2end_model')
from torch.autograd import Variable
from end2end_model.model import my_dataset
from end2end_model.model.cnn_model_v1 import CNN_v1

from tqdm import tqdm
import numpy as np

# print(type(sys.path), '\r\n'.join(sys.path))

import torch.nn as nn
from end2end_model.training_set_gen import gen_config
from end2end_model.training_set_gen import one_hot_encoding

# from end2end_model.imageProcess import toGrayscale

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print('using device:', DEVICE)

'''
arg: image_path:str,图片的路径
return: str,图片的4位识别结果
'''


def end2end_recognition(image_path):
    cnn = CNN_v1()
    cnn.eval()
    # 加载模型路径
    cnn.load_state_dict(torch.load('../back_end/imgProcess/end2end_model/model.pkl'))
    predict_dataloader = my_dataset.get_predict_data_loader()
    res = ''
    for i, (images, labels) in tqdm(enumerate(predict_dataloader)):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c0 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 0:gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c1 = gen_config.ALL_CHAR_SET[
            np.argmax(predict_label[0, gen_config.ALL_CHAR_SET_LEN:2 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c2 = gen_config.ALL_CHAR_SET[
            np.argmax(predict_label[0, 2 * gen_config.ALL_CHAR_SET_LEN:3 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c3 = gen_config.ALL_CHAR_SET[
            np.argmax(predict_label[0, 3 * gen_config.ALL_CHAR_SET_LEN:4 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        predict_label = '%s%s%s%s' % (c0, c1, c2, c3)
        res = predict_label
    return res
