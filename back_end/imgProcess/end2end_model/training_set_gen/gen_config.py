# -*- coding: UTF-8 -*-
import os
import sys
sys.path.append('.'+os.path.sep+'imgProcess'+os.path.sep)
CUR_PATH='../back_end/imgProcess/'
# 验证码中的字符
# string.digits + string.ascii_uppercase
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ALL_CHAR_SET = NUMBER + ALPHABET
ALL_CHAR_SET_LEN = len(ALL_CHAR_SET)
MAX_CAPTCHA = 4

# 图像大小
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160

# TRAIN_DATASET_PATH = os.getcwd()+os.path.sep+'dataset' + os.path.sep + 'train'
# TEST_DATASET_PATH = os.getcwd()+os.path.sep+'dataset' + os.path.sep + 'test'

# TRAIN_DATASET_PATH = "."+os.path.sep+'dataset' + os.path.sep + 'train'
# TEST_DATASET_PATH = "."+os.path.sep+'dataset' + os.path.sep + 'test'


# 06.17
TRAIN_DATASET_PATH ='/media/canvolcnao/DATA/GitHubRepos/ds/dataset/train'
TEST_DATASET_PATH = '/media/canvolcnao/DATA/GitHubRepos/ds/dataset/test'

# PREDICT_DATASET_PATH = CUR_PATH+'img/img_to_predict' # 在生产环境中，配置后端接收的要预测的图片的路径
PREDICT_DATASET_PATH='../back_end/'+'media'

DEMONSTRATION_PATH='../back_end/'+'media' # 生产环境中，配置需要为用户生成的验证码的路径
