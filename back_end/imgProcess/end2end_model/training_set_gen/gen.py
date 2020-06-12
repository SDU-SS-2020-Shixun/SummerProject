# -*- coding: UTF-8 -*-
from captcha.image import ImageCaptcha  # pip install captcha
from PIL import Image
import random
import time
import gen_config
import os
from tqdm import tqdm as td

def random_captcha():
    captcha_text = []
    for i in range(gen_config.MAX_CAPTCHA):
        c = random.choice(gen_config.ALL_CHAR_SET)
        captcha_text.append(c)
    return ''.join(captcha_text)

# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha()
    captcha_text = random_captcha()
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image

def gen_training_set(CAPTCHA_COUNT=int(1e5)):
    # CAPTCHA_COUNT = int(1e5)
    path = gen_config.TRAIN_DATASET_PATH    #通过改变此处目录，以生成 训练、测试和预测用的验证码集
    if not os.path.exists(path):
        os.makedirs(path)
    for i in td(range(CAPTCHA_COUNT)):
        now = str(int(time.time()))
        text, image = gen_captcha_text_and_image()
        filename = text+'_'+now+'.png'
        image.save(path  + os.path.sep +  filename)
        # print('saved %d : %s' % (i+1,filename))

def gen_test_set(CAPTCHA_COUNT=int(1e4)):
    # CAPTCHA_COUNT = int(1e5)
    path = gen_config.TEST_DATASET_PATH    #通过改变此处目录，以生成 训练、测试和预测用的验证码集
    if not os.path.exists(path):
        os.makedirs(path)
    for i in td(range(CAPTCHA_COUNT)):
        now = str(int(time.time()))
        text, image = gen_captcha_text_and_image()
        filename = text+'_'+now+'.png'
        image.save(path  + os.path.sep +  filename)
        # print('saved %d : %s' % (i+1,filename))


if __name__ == '__main__':
    gen_training_set(int(9e4))
    # gen_test_set()
