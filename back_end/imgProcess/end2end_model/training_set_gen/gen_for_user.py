# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import gen_config
import os
from tqdm import tqdm as td

def gen_1_image():
    # CAPTCHA_COUNT = int(1e5)
    path = gen_config.DEMONSTRATION_PATH    
    if not os.path.exists(path):
        os.makedirs(path)
    now = str(int(time.time()))
    text, image = gen_captcha_text_and_image()
    filename = text+'_'+now+'.png'
    image.save(path  + os.path.sep +  filename)
    # print('saved %d : %s' % (i+1,filename))