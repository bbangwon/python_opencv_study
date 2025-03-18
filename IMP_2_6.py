import cv2
import numpy as np

img = cv2.imread('images/scene2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

ret, img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # 127보다 크면 255, 작으면 0

# 최적의 임계값을 찾아주는 otsu 알고리즘을 적용한다.
ret, img_otsu = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 127보다 크면 255, 작으면 0, Otsu 알고리즘 적용

cv2.imshow('ResultBinary', img_binary)
cv2.imshow('ResultOtsu', img_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()