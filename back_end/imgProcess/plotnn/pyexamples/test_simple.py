# 运行：python test_simple.py
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks  import *
import subprocess
import os
import fitz
import time
# defined your arch

def gen_pnn_png(input):
    namefile = str(sys.argv[0]).split('.')[0]
    input_path='../../../media/'+input
    now = str(int(time.time()))
    print(namefile)

    # defined your arch
    arch = [
        to_head('..'),
        to_cor(),
        to_begin(),
        # to_Conv("conv1", 512, 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
        # to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
        # to_Conv("conv2", 128, 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
        # to_connection( "pool1", "conv2"),
        # to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
        # to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
        # to_connection("pool2", "soft1"),
        to_input(input_path, to='(-3,0,0)'),

        to_Conv('conv0', 3, 3, offset="(0,0,0)",to="(0,0,0)",height=32, depth=32,width=0.4),

        to_Conv('conv', 7, 64, offset="(0,0,0)",to="(0,0,0)",height=48, depth=48,width=1.2),
        to_Pool('maxpool', offset="(0,0,0)",to="(conv0-east)", height=32, depth=32),

        # l1
        to_Conv('conv1', 3, 64, offset="(0.1,0,0)", to="(maxpool-east)", height=32, depth=32, width=1.2),
        to_Conv('conv2', 3, 64, offset="(0.2,0,0)", to="(conv1-east)", height=32, depth=32, width=1.2),
        to_Conv('conv3', 3, 64, offset="(0.3,0,0)", to="(conv2-east)", height=32, depth=32, width=1.2),
        to_Conv('conv4', 3, 64, offset="(0.4,0,0)", to="(conv3-east)", height=32, depth=32, width=1.2),
        to_connection('conv0', 'conv1'),
        to_connection('conv1', 'conv2'),
        to_connection('conv2', 'conv3'),
        to_connection('conv3', 'conv4'),

        # l2
        to_Conv('conv5', 3, 128, offset="(0.5,0,0)", to="(conv4-east)", height=32, depth=32, width=1.6),
        to_Conv('conv6', 3, 128, offset="(0.6,0,0)", to="(conv5-east)", height=32, depth=32, width=1.6),
        to_Under1(),
        to_Conv('conv7', 3, 128, offset="(0.7,0,0)", to="(conv6-east)", height=32, depth=32, width=1.6),
        to_Conv('conv8', 3, 128, offset="(0.8,0,0)", to="(conv7-east)", height=32, depth=32, width=1.6),
       # to_connection('res2', 'res3'),

        #to_Conv('downsample34', 1, 128, offset="(0.5,0,0)", to="(res4-east)", height=16, depth=16,width=1.6),

       # to_connection('res3', 'downsample34'),
       # to_connection('downsample34', 'res4'),
        to_connection('conv4', 'conv5'),
        to_connection('conv5', 'conv6'),
        to_connection('conv6', 'conv7'),
        to_connection('conv7', 'conv8'),

        # l3
        to_Conv('conv9', 3, 256, offset="(0.9,0,0)", to="(conv8-east)", height=32, depth=32, width=2.0),
        to_Conv('conv10', 3, 256, offset="(1.0,0,0)", to="(conv9-east)", height=32, depth=32, width=2.0),
        to_Under2(),
        to_Conv('conv11', 3, 256, offset="(1.1,0,0)", to="(conv10-east)", height=32, depth=32, width=2.0),
        to_Conv('conv12', 3, 256, offset="(1.2,0,0)", to="(conv11-east)", height=32, depth=32, width=2.0),
        #to_connection('res4', 'res5'),

        #to_Conv('downsample56', 1, 256, offset="(0.8,0,0)", to="(res6-east)", height=16, depth=16,width=2.0),

       # to_connection('res5', 'downsample56'),
       # to_connection('downsample56', 'res6'),
        to_connection('conv8', 'conv9'),
        to_connection('conv9', 'conv10'),
        to_connection('conv10', 'conv11'),
        to_connection('conv11', 'conv12'),

        # l4

        to_Conv('conv13', 3, 512, offset="(1.3,0,0)", to="(conv12-east)", height=32, depth=32, width=2.4),
        to_Conv('conv14', 3, 512, offset="(1.4,0,0)", to="(conv13-east)", height=32, depth=32, width=2.4),
        to_Under3(),
        to_Conv('conv15', 3, 512, offset="(1.5,0,0)", to="(conv14-east)", height=32, depth=32, width=2.4),
        to_Conv('conv16', 3, 512, offset="(1.6,0,0)", to="(conv15-east)", height=32, depth=32, width=2.4),
        #to_connection('res6', 'res7'),

        #to_Conv('downsample78', 1, 512, offset="(1.1,0,0)", to="(res8-east)", height=16, depth=16,width=2.4),
        to_connection('conv12', 'conv13'),
        to_connection('conv13', 'conv14'),
        to_connection('conv14', 'conv15'),
        to_connection('conv15', 'conv16'),
       # to_connection('res7', 'downsample78'),
       # to_connection('downsample78', 'res8'),

        to_Pool('avgPool', offset="(1.7,0,0)", to="(conv16-east)"),
        to_SoftMax('fc', offset="(1.8,0,0)", to="(avgPool-east)",caption='SOFT'),
        to_connection('avgPool', 'fc'),

        to_connect1(),
        to_connect2(),
        to_connect3(),


        to_end()
    ]

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
