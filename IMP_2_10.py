import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

# 히스토그램 평활화 계산
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) # 히스토그램 계산
cdf = hist.cumsum() # 누적합 계산
cdf_m = np.ma.masked_equal(cdf, 0) # 0인 값을 mask 처리
cdf_m = (cdf_m - cdf_m.min()) / (rows * cols) * 255 # 정규화
cdf = np.ma.filled(cdf_m, 0).astype('uint8') # mask 처리된 값을 0으로 채움
print("cdf shape:", cdf.shape)
img2 = cdf[img] # 룩업 테이블을 이용한 히스토그램 평활화

# OpenCV API로 이퀄라이즈 히스토그램 적용
img3 = cv2.equalizeHist(img)

# 이퀄라이즈 결과 히스토그램 계산
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([img3], [0], None, [256], [0, 256])

# 결과 출력
cv2.imshow('Before', img)
cv2.imshow('Manual', img2)
cv2.imshow('cv2.equalizeHist()', img3)

hists = {'Before': hist, 'Manual': hist2, 'cv2.equalizeHist()': hist3}
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 3, i + 1)
    plt.plot(v)
    plt.title(k)
plt.show()