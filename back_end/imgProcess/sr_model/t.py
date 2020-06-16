import random
import train1
import numpy as np
import os
from PIL import Image
import cv2

filepath = 'D:/python program/VOC2007/test/s74k.png'
captcha_image = Image.open(filepath)
captcha_image = captcha_image.resize((160, 60))
captcha_image = np.float32(captcha_image)
img = captcha_image.flatten() / 255
output = train1.predict_captcha(img)
print("预测：" + output)
