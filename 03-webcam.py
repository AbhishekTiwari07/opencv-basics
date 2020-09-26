import cv2 as cv

vid = cv.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)
vid.set(10,100)

while True:
    success, img = vid.read()
    cv.imshow("Video",img)
    if ( cv.waitKey(1) & 0xFF == ord('q') ):
        break
vid.release()
cv.deleteAllWindows()