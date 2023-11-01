import cv2
import numpy as np
def main():
    original = cv2.imread('C:\\Users\\JangBeomJun\\Downloads\\s1-4.png', cv2.IMREAD_GRAYSCALE)
    ret, img_thresh = cv2.threshold(original,230,255,0)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    gradient = cv2.morphologyEx(img_thresh, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('JetsonNano_Contours_Original', original)
    cv2.imshow('gradient', gradient)

    resultImg = cv2.subtract(gradient,original)

    cv2.imshow('resultImg', resultImg)


    contours, hierachy = cv2.findContours(resultImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_contours = resultImg.copy()
    img_contours = cv2.drawContours(img_contours, contours, -1, (51,102,255), 2)

    cv2.imshow('img_contours', img_contours)

    rows, cols = img_contours.shape[:2]

    finalImb = cv2.putText(img_contours,str(len(contours)), (int(cols/2),int(rows/2)),cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 256), 1)


    cv2.imshow('finalImb', finalImb)

    cv2.imwrite('finalImg.png', finalImb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()