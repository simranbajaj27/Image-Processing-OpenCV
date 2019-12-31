import cv2
 
image = cv2.imread("flower.jpg")

# resizing the image to 100 x 100 px
resize = cv2.resize(image, (100, 100))
cv2.imshow("Resized", resize)
cv2.waitKey(0)
