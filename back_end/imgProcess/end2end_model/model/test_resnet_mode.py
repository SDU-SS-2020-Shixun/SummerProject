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

import torch.nn as nn
from end2end_model.training_set_gen import gen_config
from end2end_model.training_set_gen import one_hot_encoding 

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def main():
    cnn = ResNet34()
    cnn.eval()
    cnn.load_state_dict(torch.load('resnet_model.pkl'))
    print("load resnet ...")

    test_dataloader = my_dataset.get_test_data_loader()

    correct = 0
    total = 0
    for i, (images, labels) in tqdm(enumerate(test_dataloader)):
        image = images
        vimage = Variable(image)
        predict_label = cnn(vimage)

        c0 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 0:gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c1 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, gen_config.ALL_CHAR_SET_LEN:2 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c2 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 2 * gen_config.ALL_CHAR_SET_LEN:3 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        c3 = gen_config.ALL_CHAR_SET[np.argmax(predict_label[0, 3 * gen_config.ALL_CHAR_SET_LEN:4 * gen_config.ALL_CHAR_SET_LEN].data.numpy())]
        predict_label = '%s%s%s%s' % (c0, c1, c2, c3)
        true_label = one_hot_encoding.decode(labels.numpy()[0])
        total += labels.size(0)
        if(predict_label == true_label):
            correct += 1
        if(total%200==0):
            print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))
    print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))

if __name__ == '__main__':
    main()