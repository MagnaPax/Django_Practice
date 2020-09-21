import tensorflow as tf
tf.__version__

from PIL import Image
import numpy as np
import os,glob

# 모델을 불러들이기 위한 모듈
from tensorflow.compat.v2.keras.models import model_from_json


# json파일 읽어오기
json_file = open('libs/catdog_model.json')
load_model_json = json_file.read()
json_file.close()


#load_model_json => 모델화 하기
load_model = model_from_json(load_model_json)
#load_model


# 읽어온 모델에서 가중치 값 불러오기
load_model.load_weights("libs/model.h5")


# 실제 컴파일 하기 => binary_crossentropy 이진분류, adam 최적화
load_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


from tensorflow.python.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt


image = Image.open("./imgs/cat7.jpg")
width = 64
height = 64
color = 3 #색깔 갯수
image = image.resize((width, height))

plt.imshow(image)
plt.show()


# 이미지를 벡터화
image = np.array(image)
print(image.shape) #(150, 150, 3)
x_test = [image]
x_test = np.array(x_test)
x_test = x_test / 255
#print(x_test)


# 예측
y_predict = load_model.predict(x_test)


print(y_predict.flatten()[0])


print("-------------------------------------------")
category = ""
if y_predict >= 0.5:
    category = "cat"
    print("cat", y_predict)
else:
    category = "doc"
    print("dog", y_predict)



