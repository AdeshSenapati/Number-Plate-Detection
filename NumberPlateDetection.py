import cv2


##############################
width = 640
height = 480
faceCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500
##############################
count = 1
cap = cv2.VideoCapture("video.mp4")
cap.set(3, width)
cap.set(4, height)
cap.set(10, 150)
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow("NumberPlate", imgRoi)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("NumberPlate_"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Saved Scan", (150, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count = count+1
