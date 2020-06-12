## 设计思路

1. end2end
2. pytorch 实现的深度卷积神经网络
3. 进阶：LSTM+Attention+CTCLoss?



## 数据集

1. 使用 captcha API 生成。相关代码

   ![image-20200611133649815](https://i.loli.net/2020/06/11/XlRIS3sZG8qvUug.png)

2. 10万张traing_set和1万的test_set
   * 百度云
   * https://pan.baidu.com/s/10D2Pumy6WUO2xEvSmiyUkQ
   * 提取码：2gqu



## API

1. 模型文件为 model.pkl

   ![image-20200611115810725](https://i.loli.net/2020/06/11/UG3KcTekDN5CW1X.png)

2. 调用模型：

   * 首先配置后端接收到的图片的路径，并将文件重命名为 ++++_时间戳.png。(e.g., ++++_123456.png)

   ![image-20200611212310016](https://i.loli.net/2020/06/11/FRhj1zLwnUHamYl.png)

   * 然后即可调用：

   ![image-20200611212118943](https://i.loli.net/2020/06/11/zopOPyeUibRcH5C.png)

3. 为用户随机生成一张验证码：

   * 首先配置希望在后端生成的文件的路径：

   ![image-20200611212939814](https://i.loli.net/2020/06/11/bvOi6PhNVUmQTng.png)

   * 然后即可调用

![image-20200611213132715](https://i.loli.net/2020/06/11/4XPeC6qjoag91JD.png)





## CNN_v1

