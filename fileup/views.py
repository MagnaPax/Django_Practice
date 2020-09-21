# pip install tensorflow
# pip install pilllow

######################################################################
from PIL import Image
import os, glob, numpy as np
from tensorflow.python.keras.models import load_model, model_from_json
import tensorflow as tf
from tensorflow.python.keras.preprocessing.image import load_img
import matplotlib.pyplot as plt
######################################################################

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

UPLOAD_DIR ="/home/kosmo1/PycharmProjects/myweb/fileup/static/images/"
def main(request):
    return render(request, 'fileup/upform1.html')


@csrf_protect
def upload_success(request):
    # 업로드 된 파일이 있는지 검사. 파일 형태로 넘어올 때 ==> requestFILES['param']
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        fine_name = file._name # 업로드 된 파일 이름
        # wb : write binary mode
        fp = open("%s%s"%(UPLOAD_DIR, fine_name), 'wb')
        # 1byte씩 읽어들이면서 저장
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    else: # 업로드 된 파일이 없는 경우
        file_name = "-"
    return render(request, 'fileup/success1.html', {'file_name':fine_name})


def main2(request):
    return render(request, 'fileup/upform2.html')

@csrf_protect
def upload_success2(request):
    # 업로드 된 파일이 있는지 검사. 파일 형태로 넘어올 때 ==> requestFILES['param']
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        fine_name = file._name # 업로드 된 파일 이름
        # wb : write binary mode
        fp = open("%s%s"%(UPLOAD_DIR, fine_name), 'wb')
        # 1byte씩 읽어들이면서 저장
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
        ######################################################################
        json_file = open("/home/kosmo1/PycharmProjects/myweb/fileup/static/catdog_model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("/home/kosmo1/PycharmProjects/myweb/fileup/static/model.h5")
        print("Loaded model from disk")
        loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        image = Image.open("%s%s" % (UPLOAD_DIR, fine_name))
        width,height,color = 64,64,3
        image = image.resize((width, height))
        image = np.array(image)
        x_test = [image]
        x_test = np.array(x_test)
        x_test = x_test / 255
        y_predict = loaded_model.predict(x_test)
        print(y_predict)

        category = ""
        if y_predict >= 0.5:
            category = "cat"
        else:
            category = "dog"
        ######################################################################
    else: # 업로드 된 파일이 없는 경우
        file_name = "-"
    return render(request, 'fileup/success2.html', {'file_name':fine_name, 'category':category, 'y_predict':y_predict})