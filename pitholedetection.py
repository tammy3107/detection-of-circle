import numpy as np
import cv2
#setting camera port 
camera_port = 0
#setting default frames
frames = 30
camera = cv2.VideoCapture(camera_port)
while (camera.isOpened()):
    #reading image,changing to grayscale 
    ret,img= camera.read()
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    output = img.copy()
    #detecting circles in image
    circles = cv2.HoughCircles(gray,cv2.cv.CV_HOUGH_GRADIENT,1, 260, param1=30, param2=65, minRadius=0, maxRadius=0)
    
    #Ensure some circles are found
    if circles is not None:
        #Convert the (x,y) coordinate and radius of the circles
        circles = np.round(circles[0,:]).astype("int")
        
        #Loop over the  (x,y) coordinate and radius of the circles
        for (x,y,r) in circles:
            #Draw the circle in the output
            cv2.circle(output,(x,y),r,(0,255,0),4)
            
        #show the output image
        cv2.imshow("gray",gray)
        cv2.imshow("output",output)
        k = cv2.waitKey(10)
        if k==27 :
            break
