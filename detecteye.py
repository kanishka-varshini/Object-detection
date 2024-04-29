# import libraries needed: OpenCV  
import cv2

haar_cascade = 'haarcascade_eye.xml'

#initializing the video capture object
cap = cv2.VideoCapture(0) #change index for different cameras

eye_cascade = cv2.CascadeClassifier(haar_cascade) 

#loop runs till the "q" key is pressed
while True: 
    ret, frames = cap.read() #read the current frame from the video
        
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) #convert frames to greyscale
        
    eye = eye_cascade.detectMultiScale(gray, 1.2, 2) #detects eyes of different sizes in the input image, here 1.2 is the
        
    #drawing a rectangle around the object
    for (x,y,w,h) in eye: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),1) 
    
    #display the frame w rectangle
    cv2.imshow('video', frames) 
        
    #press q on the keyboard to exit 
    if cv2.waitKey(33) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()