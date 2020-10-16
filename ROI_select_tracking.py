import tensorflow as tf
import IPython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
import cv2

mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools


def tensor_to_image(tensor):
    #텐서 즉, 데이터를 이미지로 데이터가 들어오면 이미지로 바꾼당
    tensor = tensor*255 # 255 곱하는 이유는 텐서는 플로트형이라서
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1 #가정 설정문 예외처리
    
    tensor = tensor[0]
    return PIL.Image.fromarray(tensor)



content_path = tf.keras.utils.get_file('YellowLabradorLooking_new.jpg',
'https://storage.googleapis.com/download.tensorflow.org/example_images/YellowLabradorLooking_new.jpg')
# https://commons.wikimedia.org/wiki/File:Vassily_Kandinsky,_1913_-_Composition_7.jpg
style_path = tf.keras.utils.get_file('kandinsky5.jpg',
'https://storage.googleapis.com/download.tensorflow.org/example_images/Vassily_Kandinsky%2C_1913_-_Composition_7.jpg')

 #######원본 사진##########
imgpath = np.fromfile(image, np.uint8)
self.img_original = cv2.imdecode(imgpath, cv2.IMREAD_UNCHANGED)
self.img_original = cv2.cvtColor(self.img_original, cv2.COLOR_BGR2RGB)  # img = array
#print(np.shape(img)) # (w, h, scale)
self.img_original = cv2.resize(self.img_original, dsize=(285,400)) #이미지 사이즈 통일화
        
        


def imshow(image, title=None):
    if len(image.shape) > 3:
        image = tf.squeeze(image, axis=0)
    
    plt.imshow(image)
    if title:
        plt.title(title)


content_image = load_img(content_path)
style_image = load_img(style_path)

plt.subplot(1, 2, 1)
imshow(content_image, 'Content Image')

plt.subplot(1, 2, 2)
imshow(style_image, 'Style Image')
