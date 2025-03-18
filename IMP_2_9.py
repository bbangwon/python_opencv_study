import cv2
import numpy as np
import matplotlib.pyplot as plt

# 컬러영상
img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)
cv2.imshow('Image Processing', img)

#히스토그램 계산 및 그리기
channels = cv2.split(img)
colors = ('b', 'g', 'r')
for (ch, color) in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)

plt.show()