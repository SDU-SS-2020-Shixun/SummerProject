import torch
import torch.nn as nn
from torch.autograd import Variable
import sys
# 修改文件导入路径
sys.path.append('../back_end/imgProcess')
import end2end_model.model.my_dataset
from end2end_model.model.cnn_model_v1 import CNN_v1
import sys
from tqdm import tqdm
import numpy as np
import os 


# print(type(sys.path), '\r\n'.join(sys.path))

import torch.nn as nn
from end2end_model.training_set_gen import gen_config
from end2end_model.training_set_gen import one_hot_encoding 
from end2end_model.imageProcess import toGrayscale

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print('using device:',DEVICE)

'''
arg: image_path:str,图片的路径
return: str,图片的4位识别结果
'''
def end2end_recognition(image_path):
    cnn = CNN_v1()
    cnn.eval()
    cnn.load_state_dict(torch.load('model.pkl'))
    print('加载CNN_V1模型')
    predict_dataloader = my_dataset.get_predict_data_loader()
    res=''
    for i, (images, labels) in tqdm(enumerate(predict_dataloader)):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c0 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 0:gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c1 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, gen_config.ALL_CHAR_SET_LEN:2 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c2 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 2 * gen_config.ALL_CHAR_SET_LEN:3 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c3 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 3 * gen_config.ALL_CHAR_SET_LEN:4 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        predict_label = '%s%s%s%s' % (c0, c1, c2, c3)
        res=predict_label
    return res
