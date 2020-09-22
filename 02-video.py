import cv2 as cv

vid = cv.VideoCapture("resources/sampleVideo.mp4")

while True:
    success, img = vid.read()
    cv.imshow("Video",img)
    if ( cv.waitKey(1) & 0xFF == ord('q') ):
        break