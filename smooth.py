import cv2

blur_size = (30, 30)
img = cv2.imread('./images/sample.jpg')

img = cv2.blur(img, blur_size)
cv2.imwrite('./trans_images/smooth/sample01.jpg', img)