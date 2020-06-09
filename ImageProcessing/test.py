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
    #for i in range(0,len(filelist)):

    filename = filelist[index]
    file_path = os.path.join(file_dir,filename)
    img = Image.open(file_path).convert("RGB")
    img = img.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    img = np.array(img)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret3, th3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY +
                              cv2.THRESH_OTSU)
    captcha_image = np.array(th3)
    captch_text = filename.split(".")[0]

    img = Image.fromarray(captcha_image.astype('uint8'))
    vertical(img,captch_text)
    plt.imshow(img, cmap='Greys_r')
    plt.show()
    #cv2.imwrite("../yzm_after_process/" + captch_text + ".png", captcha_image)
#return captch_text,captcha_image

def vertical(img,text):

    pixdata = img.load()
    w,h = img.size
    ver_list = []

    for x in range(w):
        black = 0
        for y in range(h):
            if pixdata[x,y] == 0:
                black += 1

        ver_list.append(black)

    l,r = 0,0
    flag = False
    cuts = []
    for i,count in enumerate(ver_list):

        if flag is False and count > 10:
            l = i
            flag = True
        if flag and count == 0:
            r = i-1
            flag = False
            cuts.append((l,r))

        if i==(w-1) and flag == True:
            cuts.append((l,w))


    v = cuts
    j = 0

    for i,n in enumerate(v,l):

        width = (n[1] - n[0])
        threshold = IMAGE_WIDTH * 0.08

        if width > threshold:
            temp = img.crop((n[0],0,n[1],IMAGE_HEIGHT))

            WHITE = [255, 255, 255]
            temp = np.array(temp)
            temp = cv2.copyMakeBorder(temp,0,0,6,6,cv2.BORDER_CONSTANT,value=WHITE)
            temp = Image.fromarray(temp.astype('uint8'))

            temp.save("../cut/" + text[j] + ".png")
            j += 1

        # return cuts


if __name__ == '__main__':

    file_dir = '../yzm'
    get_captcha_text_and_image(file_dir)
    # text,image = get_captcha_text_and_image(file_dir)
    # print(text)
    #
    # plt.imshow(image, cmap='Greys_r')
    # plt.show()
