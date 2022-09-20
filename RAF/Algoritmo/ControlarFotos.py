from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import os

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Webcam", frame)
        key = cv2.waitKey(1)
        if key == 113: #q
            os.system('cls')
            break
    cv2.imwrite("./Fotos/Img.jpg", frame)

webcam.release()
cv2.destroyAllWindows()

capitura = cv2.VideoCapture(0)
capitura.set(3, 1270)
capitura.set(3, 720)

detector = FaceMeshDetector(maxFaces = 2)

while True:
    sucesso, frame = capitura.read()
    frame, faces = detector.findFaceMesh(frame)

    if faces:

        print(faces[0])

        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            os.system('cls')
            break
        cv2.imwrite("./Fotos/Frame.jpg", frame)

capitura.release()
cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
capitura = cv2.VideoCapture(0)

while True:
    sucesso, imagem = capitura.read()

    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (0, 0, 0), 3)

    cv2.imshow('Webcam', imagem)

    key = cv2.waitKey(1) & 0xff
    if key == 113: #q
        os.system('cls')
        break
        
capitura.release()
cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

imagem = cv2.imread('./Fotos/Img.jpg')

gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 0, 0), 3)

    print('==================================================')
    print('       Reconhecimento de faces com imagens')
    print('==================================================')

cv2.imshow('Imagem', imagem)
cv2.waitKey()