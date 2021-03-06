# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import sys
# 修改文件导入路径

CUR_PATH='../back_end/imgProcess'
sys.path.append('../back_end/imgProcess/')
import time
from end2end_model.training_set_gen import gen, gen_config
import os
from tqdm import tqdm as td

def gen_1_image():
    # CAPTCHA_COUNT = int(1e5)
    path = gen_config.DEMONSTRATION_PATH    
    if not os.path.exists(path):
        os.makedirs(path)
    now = str(int(time.time()))
    text, image = gen.gen_captcha_text_and_image()
    filename = text+'_'+now+'.png'
    imgPath = path  + os.path.sep +  filename
    image.save(imgPath)
    return imgPath
    # print('saved %d : %s' % (i+1,filename))