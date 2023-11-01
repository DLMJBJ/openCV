import cv2
import numpy as np
from matplotlib import pyplot as plt


def main() :
    img = cv2.imread('C:\\Users\\JangBeomJun\\Desktop\\photo\\a65b87a6a5c139d404f8078432c64390.jpg', cv2.IMREAD_COLOR)
    rows, cols = img.shape[:2]

    pts1 = np.float32([[int(cols/4), int(rows/4)],[int((cols*3)/4), int(rows/4)],[int(cols/4), int((rows*3)/4)]])
    pts2 = np.float32([[int(cols/4),int((rows*3)/8)],[int((cols*3)/4),int(rows/8)],[int(cols/4),int((rows*7)/8)]])

    cv2.circle(img, (int(cols/4), int(rows/4)), 10, (255, 0, 0), -1)
    cv2.circle(img, (int((cols*3)/4), int(rows/4)), 10, (0, 255, 0), -1)
    cv2.circle(img, (int(cols/4), int((rows*3)/4)), 10, (0, 0, 255), -1)

    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))



    
    cv2.imshow('IMAGE',img)
    cv2.imshow('AFFINE',dst)

    cv2.waitKey(0)  
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()