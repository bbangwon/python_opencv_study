import cv2
import numpy as np

img = cv2.imread('images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

blk_size = 9    # 블럭 사이즈
C = 5          # 차감 상수
ret, img_otsu = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 127보다 크면 255, 작으면 0, Otsu 알고리즘 적용
img_a1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, C) # 평균값 사용
img_a2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C) # 가우시안 가중치 사용

cv2.imshow('ResultOtsu', img_otsu)
cv2.imshow('ResultAdaptive1', img_a1)
cv2.imshow('ResultAdaptive2', img_a2)

cv2.waitKey(0)
cv2.destroyAllWindows()