import numpy as np
import cv2
 
image = cv2.imread("image.jpeg")
boundaries = {
	"red":(np.array([17, 15, 100]),np.array([50, 56, 200])),
	"blue":(np.array([86, 31, 4]), np.array([220, 88, 50])),
	"yellow":(np.array([25, 146, 190]),np.array([62, 174, 250])),
	"gray":(np.array([103, 86, 65]), np.array([145, 133, 128])),
	"green":(np.array([60,60,65]),np.array([255,255,80]))
}

for (lower, upper) in boundaries.items():
  mask = cv2.inRange(image, upper[0], upper[1])
  output = cv2.bitwise_and(image, image, mask = mask)
  ret,thrshed = cv2.threshold(cv2.cvtColor(output,cv2.COLOR_BGR2GRAY),3,255,cv2.THRESH_BINARY)
  _,contours, hierarchy = cv2.findContours(thrshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
  for cnt in contours:
    area = cv2.contourArea(cnt)
    if area >60:	
     cv2.putText(image,lower, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
     cv2.rectangle(image,(5,40),(400,100),(0,255,255),2)
     cv2.imshow('frame',image)   
  cv2.waitKey(0)