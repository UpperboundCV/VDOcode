import cv2
import sys
import os
import argparse
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
ap.add_argument("-p", "--path", required=True,
	help="path of Image")
args = vars(ap.parse_args())
 
# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))

# cascPath = sys.argv[1]
cascPath = 'C:/opencv-3.4.3/opencv-3.4.3/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(1)
count = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    # Capture frame-by-frame
    ret, frame   = video_capture.read()
    height, width, channels = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    if not os.path.exists(args['path']):
        os.mkdir(args['path'])

    biggest = 0
    countFace = 0
    FaceNum = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        if w*h > biggest:
            biggest = w*h
            FaceNum = countFace
        countFace += 1
            
    countFace = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        if FaceNum == countFace:
            up = y
            if y-round(0.2*h)>0:
                up = int(y-round(0.2*h))
            bottom = y+h
            if y+round(1.2*h)<height:
                bottom = int(y+round(1.2*h))
            left = x 
            if x-round(0.2*w)>0:
                left = int(x-round(0.2*w))
            right = x+w
            if x+round(1.2*w)<width:
                right = int(x+round(1.2*w))
            cv2.imwrite(args['path'] + '/' +args['name']+str(count)+'.jpg',frame[up:bottom,left:right])
            cv2.rectangle(frame, (left, up), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame,str(w)+str('x')+str(h),(left,up), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.putText(frame,str(width)+str('x')+str(height),(0,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            print('Take: ' + str(count) + ' images')
            count+=1
        countFace += 1
        


    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # cv2.imwrite(args['path']+'/'+args['name']+str(count),frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if count==240:
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()