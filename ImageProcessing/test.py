import os
import cv2
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
IMAGE_HEIGHT = 60
IMAGE_WIDTH  = 160

def get_captcha_text_and_image(file_dir):
    filelist = os.listdir(file_dir)
    index = random.randint(0, len(filelist) - 1)
    for i in range(0,len(filelist)):

        filename = filelist[i]
        file_path = os.path.join(file_dir,filename)
        img = Image.open(file_path).convert("RGB")
        img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
        img = np.array(img)

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        ret3, th3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY +
                              cv2.THRESH_OTSU)
        captcha_image = np.array(th3)
        captch_text = filename.split(".")[0]
        cv2.imwrite("../yzm_after_process/" + captch_text + ".png", captcha_image)
    #return captch_text,captcha_image

if __name__ == '__main__':

    file_dir = '../yzm'
    get_captcha_text_and_image(file_dir)
    # text,image = get_captcha_text_and_image(file_dir)
    # print(text)
    #
    # plt.imshow(image, cmap='Greys_r')
    # plt.show()


# # 图1
# img = cv2.imread('../yzm/0a21.png')
# # 图2
# img2 = cv2.imread('../yzm/0a94.png')
# # 图集
# imgs = np.hstack([img, img2])
# # 展示多个
# cv2.imshow("mutil_pic", imgs)
# # 等待关闭
# cv2.waitKey(0)


# path = "./yzm提供"   #图像读取地址
# filelist = os.listdir(path)  # 打开对应的文件夹
# otal_num = len(filelist)  #得到文件夹中图像的个数
#
# print(otal_num)