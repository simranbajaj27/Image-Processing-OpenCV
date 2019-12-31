# import the necessary packages
import cv2
 
# load the input image 
image = cv2.imread("flower.jpg")

#save the image 
cv2.imwrite('flower_new',image)

# display the image to the screen 
cv2.imshow("Image", image)
cv2.waitKey(0)
