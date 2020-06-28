# 运行：python test_simple.py
import sys
sys.path.append('../')
from pycore.tikzeng import *
import subprocess
import os
import fitz
import time
# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    to_connection( "pool1", "conv2"), 
    to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    to_connection("pool2", "soft1"),    
    to_end()
    ]
def gen_pnn_png():
    namefile = str(sys.argv[0]).split('.')[0]
    now = str(int(time.time()))
    print(namefile)
    to_generate(arch, namefile + '.tex')
    proc = subprocess.Popen(['pdflatex', namefile + '.tex'])  # 启动一个新进程，相当于在命令行下 "pdflatex xx.tex"
    proc.communicate()  # 进程的交互
    os.unlink(namefile + '.tex')  # 删除中间结果，下同
    os.unlink(namefile + '.aux')
    os.unlink(namefile + '.log')
    pdf = fitz.open(namefile + '.pdf')
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(5, 5).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pnn_imgPath = '../../../media/' + now + ".png"
        pm.writePNG(pnn_imgPath)
    pdf.close()
    os.unlink(namefile + '.pdf')
    return pnn_imgPath


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    now = str(int(time.time()))
    print(namefile)
    to_generate(arch, namefile + '.tex')
    proc = subprocess.Popen(['pdflatex', namefile + '.tex'])  # 启动一个新进程，相当于在命令行下 "pdflatex xx.tex"
    proc.communicate()  # 进程的交互
    os.unlink(namefile + '.tex')  # 删除中间结果，下同
    os.unlink(namefile + '.aux')
    os.unlink(namefile + '.log')
    pdf = fitz.open(namefile + '.pdf')
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(5, 5).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pnn_imgPath = '../../../media/' + now + ".png"
        pm.writePNG(pnn_imgPath)
    pdf.close()
    os.unlink(namefile + '.pdf')
    return pnn_imgPath


if __name__ == '__main__':
    main()
