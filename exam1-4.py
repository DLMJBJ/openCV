import cv2
import numpy as np

def main() :
    image = cv2.imread('C:\\Users\\JangBeomJun\\Downloads\\urbanbrush-20210220212407818839.jpg')
    height, width, _ = image.shape
    gray_image = np.zeros((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            if y>int(height*(1/4)) and y<int(height*(1/2)) :
                if x>int(width*(1/4)) and x<int(width*(1/2)):
                    blue, green, red = image[y, x]
                    gray_value = int(red+green+blue)/3
                    gray_image[y, x] = gray_value
            

    cv2.imwrite('GrayImage.png', gray_image)

    cv2.imshow('Gray Image', gray_image)
    cv2.imshow('원본 Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()