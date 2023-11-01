import cv2
import numpy as np

def tracking():
    frame = cv2.imread('C:\\Users\\JangBeomJun\\Downloads\\photo-1595126739121-68ab4225f9cf.jpg')
    frame = cv2.resize(frame,(640, 480))

    cv2.imshow('sad;f',frame)

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('fsda',hsv)

    lower_red = np.array([40, 50, 0])
    upper_red = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow("JetsonNano_OT_Mask", mask)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    cv2.imshow("JetsonNano_OT_Result", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()