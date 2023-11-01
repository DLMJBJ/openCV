import cv2
import numpy as np

def image_translation():
    img = cv2.imread('C:\\Users\\JangBeomJun\\Desktop\\unnamed.jpg', cv2.IMREAD_COLOR)
    rows, cols = img.shape[:2]
    img = cv2.rectangle(img, (0, 0), (cols-1, rows-1), (255, 255, 255), 1)
    M = np.float32([[12, 5, 10], [0, 1, 20]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('JetsonNano_Original', img)
    cv2.imshow('JetsonNano_Translation', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()