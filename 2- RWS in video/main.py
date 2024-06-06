import cv2

cap = cv2.VideoCapture(0)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fourcc = cv2.VideoWriter_fourcc(*"XVID") #codec video id (fourcc)
outputVideo = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    cv2.imshow("Cam", frame)

    outputVideo.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
outputVideo.release()
cv2.destroyAllWindows()
