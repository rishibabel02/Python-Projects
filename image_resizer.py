import cv2


src = cv2.imread("1692515326994.jpg",cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)
# percent by which scale is resized 
scale_percent = 50
# calculate the 50 % of original
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

dsize = (width , height)

output = cv2.resize(src,dsize)

cv2.imwrite('newimage.jpg',output)
cv2.waitKey(0)