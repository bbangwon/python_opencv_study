import cv2
import numpy as np
import matplotlib.pyplot as plt

#컬러영상 읽기
img = cv2.imread('images/low_contrast.jpg', cv2.IMREAD_COLOR)

#컬러영상을 HSV로 변환
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#V(밝기값) 공간에 히스토그램 평활화 적용
img_hsv[:,:, 2] = cv2.equalizeHist(img_hsv[:,:, 2])

#HSV를 BGR로 다시 변환
img2 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

#결과 출력
cv2.imshow('Before', img)
cv2.imshow('After', img2)

cv2.waitKey()
cv2.destroyAllWindows()
