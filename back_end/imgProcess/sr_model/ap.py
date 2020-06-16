import tensorflow as tf
import numpy as np
import train1
import os
from PIL import Image

sess = tf.Session()
X = None  # input
yhat = None  # output


def load_model():
    """
        Loading the pre-trained model and parameters.
    """
    global X, yhat
    modelpath = r'D:/python program/yanzhengma/'
    saver = tf.train.import_meta_graph(modelpath + 'crack_capcha_2.model-1800.meta')
    saver.restore(sess, tf.train.latest_checkpoint(modelpath))
    graph = tf.get_default_graph()
    tensor_name_list = [tensor.name for tensor in graph.as_graph_def().node]
    print(tensor_name_list)
    X = graph.get_tensor_by_name("Placeholder:0")
    yhat = graph.get_tensor_by_name("Placeholder_1:0")
    print('Successfully load the pre-trained model!')


def predict(captcha_image):
    predict = tf.argmax(tf.reshape(yhat, [-1, train1.MAX_CAPTCHA, train1.CHAR_SET_LEN], 2))
    text_list = sess.run(predict, feed_dict={X: [captcha_image], train1.keep_prob: 1})
    text = text_list[0].tolist()
    vector = np.zeros(train1.MAX_CAPTCHA * train1.CHAR_SET_LEN)
    i = 0
    for n in text:
        vector[i * train1.CHAR_SET_LEN + n] = 1
        i += 1
    return train1.vec2text(vector)


load_model()
filepath = 'D:/python program/VOC2007/test/'
file_list = os.listdir(filepath)
print(len(file_list))
right = 0
total = len(file_list)
for i in range(0, len(file_list) - 1):
    filename = file_list[i]
    text = filename.split(".")[0]
    file_path = os.path.join(filepath, filename)
    captcha_image = Image.open(file_path)
    captcha_image = captcha_image.resize((160, 60))
    captcha_image = np.float32(captcha_image)
    img = captcha_image.flatten() / 255
    output = predict(img)
    print(output)
    if output == text:
        right += 1

    print("预测：" + output + ",原本：" + text)
print("正确率为")
print(right / total)

