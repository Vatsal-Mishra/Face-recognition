import cv2    #importing the module
c=0
detect=cv2.CascadeClassifier("copy of haarcascade_frontalface_default.xml") # getting the copy of harcascading file
imp_img=cv2.VideoCapture(0)      #capturing the vedio and focusing on all the faces
while(True):
    res,img=imp_img.read()      #reading the image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #changing the colour of image to Gray
    faces=detect.detectMultiScale(gray,1.3,5)   #detecting the faces
    for (x,y,w,h) in faces:       #loop for different values
         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)   # taking all the sides to form rectangle
         cv2.imshow("Display",img)           #display

    if cv2.waitKey(1) and  0xFF == ord('q'):   # to close the recording press q
         break

imp_img.release()
cv2.destroyAllWindows()
