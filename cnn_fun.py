import json
import numpy as np
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import cv2

model=tf.keras.models.load_model(R'C:\testproject\pill_my_heart\pill_mobilenetv2_re.h5')

# file_path = r"C:\testproject\pill_my_heart\pill_className.json"

# with open(file_path, 'rt') as file:
#     data = json.load(file)
#     print(type(data))
#     print(data)
#     print(data['info']['DRUG_SHAPE'])
#     print(data['info']['COLOR_CLASS'])
#     print(data['info']['LINE'])
#     print(data['info']['SHAPE_CODE'])

data={"info": {
		"DRUG_SHAPE": [
			"기타",
			"반원형",
			"사각형",
			"삼각형",
			"원형",
			"육각형",
			"장방형",
			"타원형",
			"팔각형"
		],
		"COLOR_CLASS": [
			"갈색",
			"갈색, 투명",
			"검정",
			"남색",
			"노랑",
			"노랑, 투명",
			"보라",
			"분홍",
			"분홍, 투명",
			"빨강",
			"빨강, 투명",
			"연두",
			"연두, 진한",
			"자주",
			"주황",
			"청록",
			"초록",
			"투명",
			"파랑",
			"파랑, 옅은",
			"하양",
			"하양, 주황, 투명",
			"하양, 초록",
			"하양, 초록, 투명",
			"하양, 투명",
			"회색",
			"회색, 진한"
		],
		"LINE": [
			"+",
			"-",
			"기타",
			"정보없음"
		],
		"SHAPE_CODE": [
			"경질캡슐",
			"껌",
			"서방정",
			"서방캡슐",
			"설하정",
			"연질캡슐",
			"장용정",
			"장용캡슐",
			"저작정(츄어블정)",
			"정보없음",
			"정제",
			"좌제",
			"트로키제"
		]
	}}


def padding(img, set_size):
    try:
        h, w, c = img.shape
    except:
        print('파일을 확인후 다시 시작하세요.')
        raise

    if h < w:
        new_width = set_size
        new_height = int(new_width * (h / w))
    else:
        new_height = set_size
        new_width = int(new_height * (w / h))

    if max(h, w) < set_size:
        img = cv2.resize(img, (new_width, new_height), cv2.INTER_CUBIC)
    else:
        img = cv2.resize(img, (new_width, new_height), cv2.INTER_AREA)

    try:
        h, w, c = img.shape
    except:
        print('파일을 확인후 다시 시작하세요.')
        raise

    delta_w = set_size - w
    delta_h = set_size - h
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)

    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    return new_img

def CNN_FUN(img):
    # img1=Image.open('/content/drive/MyDrive/Untitled Folder1/1204_0.jpg')
    # img=img.resize((180,180))
    # imgArr=np.array(img)
    newimg=img.reshape(1,736,736,3)
    re=model.predict(newimg)
    # print(len(re))
    print('DRUG_SHAPE: '+data['info']['DRUG_SHAPE'][np.argmax(re[0])])
    print('COLOR_CLASS: '+data['info']['COLOR_CLASS'][np.argmax(re[1])])
    print('LINE: '+data['info']['LINE'][np.argmax(re[2])])
    print('SHAPE_CODE: '+data['info']['SHAPE_CODE'][np.argmax(re[3])])

    return {'DRUG_SHAPE':data['info']['DRUG_SHAPE'][np.argmax(re[0])],
            'COLOR_CLASS': data['info']['COLOR_CLASS'][np.argmax(re[1])],
            'LINE': data['info']['LINE'][np.argmax(re[2])],
            'SHAPE_CODE': data['info']['SHAPE_CODE'][np.argmax(re[3])],
            }


def RESHAPE_PADDING(img):
    h1,w1,c1=img.shape
    if h1>=w1:
        img1_resize=cv2.resize(img,(int(736/h1*w1),736))
    else:
        img1_resize=cv2.resize(img,(736,int(736/w1*h1)))

    return padding(img1_resize, 736)
