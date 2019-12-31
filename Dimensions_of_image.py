import imutils
import cv2
 
# images are represented as a NumPy array
# shape =[no. rows (height) , no. columns (width) ,no. channels (depth)]
image = cv2.imread("jp.png")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
 
cv2.imshow("Image", image)
cv2.waitKey(0
