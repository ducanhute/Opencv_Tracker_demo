import cv2 as cv
import numpy as np 

img = cv.imread("data/corners.jpg",cv.IMREAD_ANYCOLOR)
gray =  cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# Using tomashi algorithm to detect key point: Giong thuat toan harri nhung nang cap hon ow phan xet sai so
corners = cv.goodFeaturesToTrack(gray,50,0.2,10)
# 50: max so diem keypoint-- 0.1: gia tri nguong vung co gia tri rieng nho hon nguong se bi reject-10:khoang cach toi thieu giua 2 keypoint
# thuat toan tra ve toa do diem cua keypoint 
corners =np.int0(corners)# chuyen ve dang so nguyen
print(corners.shape)
print(len(corners))
a= corners[0]
print("a:",a)
print("a ravel",a.ravel())
a=a[0]
print("a[0]",a)

for i in corners:
    x,y = i.ravel()
    print("ravel",i.ravel())
    cv.circle(img,(x,y),3,(0,0,255),1)
# # Using harris algorithm to detect conner- keypoiton
# gray = np.float32(gray)
# dst = cv.cornerHarris(gray,2,3,0.04) # block size: khoang dichj chuyen cua window, kerner_size = kichs thuoc o windown
# # he so thu 4 k= 0.04 he so loc cua ham sobel de chuyen ve tam hinh lien quan den vien va canh
# # ham tra ve 1 buc anh dst moi pixel trong dst la sai so cua ham harris tinh dc 
# img[dst>0.1*dst.max()] =[0, 0, 255] # tai nhung cho intensity lon hon 0.5% max chuyen ve mau do


cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()