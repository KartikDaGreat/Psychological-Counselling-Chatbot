import cv2
from deepface import DeepFace
import time
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(2, cv2.CAP_DSHOW)
if (video.isOpened()):
    temptime = time.time()
while video.isOpened():
    _,frame=video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for x, y, w, h in face:
        image = cv2.rectangle(frame, (x, y), (x+w, y + h), (89, 2, 236), 1)
        analyze=DeepFace.analyze(frame, actions=['emotion'],enforce_detection=False)
        print(analyze[0]['dominant_emotion'])
    cv2.imshow('video', frame)
    if (time.time() == temptime+10):
        break
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()