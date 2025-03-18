import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 그레이 스케일로 읽어온다.
img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

# 히스토그램 계산 및 그리기
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

print("hist shape:", hist.shape) # 히스토그램의 shape (256, 1)
print("hist.sum():", hist.sum(), "img.shape:", img.shape) # 히스토그램의 총합과 이미지의 shape
plt.show()