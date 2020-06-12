from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.conf import settings

from PIL import Image
import os
import json
import time
import sys
from end2end_model.model import invoke_the_model
# 设置导包路径
sys.path.append('../back_end/imgProcess')


def upload(request):
    if request.method == 'POST':
        img = request.FILES.get("img")
        imgPath = saveImg(img)
        # 调用图形处理接口获取结果
        imgCode = invoke_the_model.end2end_recognition("")
        result = {
            "code": 200,
            "imgCode": imgCode
        }
        return HttpResponse(json.dumps(result))
    else:
        return HttpResponse(json.dumps({"code": 400, "imgCode": "request method not valid"}))


def createImg(request):
    # 调用方法获取图片路径，直接返回给前端
    imgPath = None
    imgCode = ""
    result = {
        "code": 200,
        "img": imgPath,
        "imgCode": imgCode
    }
    return HttpResponse(json.dumps(result))


# 存储图片到本地，并返回图片路径
def saveImg(img):
    imgName = img.name
    img = Image.open(img)
    # 获取文件名
    name = os.path.splitext(imgName)[0]
    imgName = name + "_" + str(time.time()) + ".png"
    imgPath = "media/" + imgName
    img.save(imgPath)
    return imgPath
