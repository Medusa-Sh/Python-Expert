import cv2
from  matplotlib import pyplot
import matplotlib
image = cv2.imread('example.jpg')
h, w = image.shape[:2]
cv2.imread('example.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image_bgr=cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_resized_image = cv2.resize(rotated_image, (w, h))

brightened_image = cv2.convertScaleAbs(image, alpha=1.5, beta=50)

combined_image = cv2.hconcat([image, gray_image_bgr, rotated_resized_image, brightened_image])

cv2.imshow('Combined Image', combined_image)
cv2.imshow('Original Image', image)

wait_key = cv2.waitKey(0)
cv2.destroyAllWindows()