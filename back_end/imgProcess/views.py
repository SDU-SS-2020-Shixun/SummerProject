from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
import urllib.request

import sys
import os

sys.path.append('.' + os.path.sep + 'imgProcess' + os.path.sep)
CUR_PATH = '../back_end/imgProcess'
# print(os.path.abspath(__file__))
print(os.getcwd())

from PIL import Image

import json
import time

# from SummerProject.Test1 import a1
# from back_end import imgProcess

from end2end_model.model import invoke_the_model
from end2end_model.training_set_gen import gen_for_user
from end2end_model.imageProcess import toGrayscale
from sr_model import ocr


# 设置导包路径
# sys.path.append('../back_end/imgProcess')

def index(request):
    return render(request, "front_end/index.html")


def upload(request):
    if request.method == 'POST':
        img = request.FILES.get("img")
        # 保存前首先清空当前文件夹下的所有图片
        del_file('media/')
        imgPath = saveImg(img)
        # 调用第一种方式获取验证码，调用图形处理接口获取结果
        imgCode1 = invoke_the_model.end2end_recognition("")
        # imgCode1 = ""
        # 调用第二种识别方法获取验证码
        imgCode2 = ocr.captcha_predict(imgPath)

        result = {
            "code": 200,
            "imgCode1": imgCode1,
            "imgCode2": imgCode2
        }
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse(json.dumps({"code": 400}))


def createImg(request):
    # 清除文件夹下的图片
    del_file('media/')
    # 调用方法获取图片路径，直接返回给前端
    imgPath = gen_for_user.gen_1_image()
    # 根据路径获取到图片文件名，前端根据文件名进行展示
    imgFile = imgPath.split("/")[-1]
    imgCode1 = invoke_the_model.end2end_recognition("")
    imgCode2 = invoke_the_model.end2end_recognition_gy("")
    result = {
        "code": 200,
        "img": imgFile,
        "imgCode1": imgCode1,
        "imgCode2": imgCode2
    }
    return HttpResponse(json.dumps(result))


def downloadImg(request):
    del_file('media/')
    imgUrl = request.GET.get("imgUrl")
    print(imgUrl)
    filePath = os.getcwd()
    print(filePath)
    savePath = os.path.join(filePath, 'media/')
    print(savePath)
    imgName = r"{0}0000_{1}.png".format(savePath, str(int(time.time())))
    urllib.request.urlretrieve(imgUrl, imgName)
    name = imgName.split("/")[-1]
    imgCode1 = invoke_the_model.end2end_recognition("")
    imgCode2 = ocr.captcha_predict("media/" + name)
    result = {
        "code": 200,
        "img": name,
        "imgCode1": imgCode1,
        "imgCode2": imgCode2
    }
    return HttpResponse(json.dumps(result))


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


# 存储图片到本地，并返回图片路径
def saveImg(img):
    imgName = img.name
    img = Image.open(img)
    img = img.resize((160, 60), Image.ANTIALIAS)
    # 获取文件名
    name = os.path.splitext(imgName)[0]
    # imgName = name + "_" + str(time.time()) + ".png" 
    # 接受到用户上传的图片后，重命名为 '0000_时间戳.png'
    imgName = '0000_' + str(time.time()) + ".png"
    imgPath = "media/" + imgName
    img.save(imgPath)

    # imgRes=toGrayscale.get_grayscale_image(imgPath)
    # img=Image.fromarray(imgRes)
    # img.save(imgPath)

    return imgPath
