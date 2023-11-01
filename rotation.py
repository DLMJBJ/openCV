import cv2
import numpy as np

def image_rotation():
    img = cv2.imread('C:\\Users\\JangBeomJun\\Desktop\\unnamed.jpg', cv2.IMREAD_COLOR)
    rows, cols = img.shape[:2]
    img = cv2.rectangle(img, (0, 0), (cols-1, rows-1), (255, 255, 255), 1)

    M = cv2.getRotationMatrix2D((cols/2,rows/2),120,0.5)
    dst = cv2.warpAffine(img,M,(cols,rows))

    cv2.imshow('JetsonNano_Original', img)
    cv2.imshow('JetsonNano_Rotation', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()