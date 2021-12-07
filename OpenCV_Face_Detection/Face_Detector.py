import cv2

# Loading pre_train Haar classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturing video from cam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Video is being analyzed frame by frame -> as image
while True:
    _, img = cap.read()

    # To gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.05, 8)

    # Draw rectangle from (x,y) coordinates, wide and high as (w,h)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    # Exit by pressing ESC key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()