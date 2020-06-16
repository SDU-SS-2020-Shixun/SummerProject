from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
import os

IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160


def captcha_pretreat(file_path):
    # 验证码去噪
    img = Image.open(file_path).convert("RGB")
    img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    img = np.array(img)

    # 灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 中值滤波
    # blur = cv2.medianBlur(gray, 3)

    # 自适应阈值二值化
    # th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 5)

    # 设置膨胀腐蚀核，矩阵 2x2
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

    # 图像膨胀
    # dilated = cv2.dilate(th3, kernel)

    # 闭运算
    # closed_op = cv2.erode(dilated, kernel)
    ret3, th3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # captcha_image = np.array(closed_op)
    captcha_image = np.array(th3)
    return captcha_image


def vertical(img):
    # 传入二值化后的图片，进行垂直投影，返回投影的切割范围
    pixdata = img.load()
    w, h = img.size
    ver_list = []

    # 开始投影
    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x, y] == 0:
                black += 1
        ver_list.append(black)

    # 判断边界
    l, r = 0, 0
    flag = False
    cuts = []
    for i, count in enumerate(ver_list):
        # 阈值这里为0
        if flag is False and count > 0:
            l = i
            flag = True
        if flag and count == 0:
            r = i - 1
            flag = False
            cuts.append((l, r))
        # 针对验证码最后一个字符已经占了图片边缘的情况，使用如下的判断条件切割下来
        if i == (w - 1) and flag == True:
            cuts.append((l, w))
    # print(cuts)
    return cuts


def captcha_predict(file_path):
    # 预测输入的图片验证码
    image = captcha_pretreat(file_path)
    img = Image.fromarray(image.astype('uint8'))
    v = vertical(img)
    code = ""
    for i, n in enumerate(v, 1):
        width = (n[1] - n[0])
        threshold = IMAGE_WIDTH * 0.05  # 设置阈值，认为切割出来得图片不足图片总宽度的5%，则认为是噪声
        if width > threshold:
            temp = img.crop((n[0], 0, n[1], IMAGE_HEIGHT))  # 调用crop函数进行切割
            # 图片扩张，在两边分别填充密度为6的白色像素点
            # WHITE = [255, 255, 255]
            # temp = np.array(temp)
            # temp = cv2.copyMakeBorder(temp, 0, 0, 6, 6, cv2.BORDER_CONSTANT, value=WHITE)
            # temp = Image.fromarray(temp.astype('uint8'))
            # temp.save("cut%s.png" % i)  # 保存切割的图片
            # 调用ocr库，语言英文，识别单个字符
            str_temp = pytesseract.image_to_string(temp, lang="eng", config="--psm 8")
            str_temp = str_temp.replace(" ", "")
            # print(str_temp)
            if str_temp.isalpha() or str_temp.isdigit():
                code = code + str_temp
    return code


