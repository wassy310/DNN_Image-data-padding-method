import cv2
import numpy as np

img = cv2.imread('./images/sample.jpg')

gamma = 0.4
imax = img.max()

img = imax * (img / imax) ** (1 / gamma)
cv2.imwrite('./trans_images/gamma/sample01.jpg', img)