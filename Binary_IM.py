import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_binary() :
    img = cv2.imread('C:\\Users\\JangBeomJun\\Downloads\\photo-1595126739121-68ab4225f9cf.jpg',cv2.IMREAD_GRAYSCALE)

    ret,dst = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
    ret,dst1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)
    ret,dst2 = cv2.threshold(img,150,255,cv2.THRESH_TRUNC)
    ret,dst3 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO)
    ret,dst4 = cv2.threshold(img,150,255,cv2.THRESH_TOZERO_INV)
    
    

    titles = ['ORIGINAL', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, dst, dst1, dst2, dst3, dst4]
    fig = plt.figure()
    fig.canvas.set_window_title('JetsonNano_Thresholding')
    for i in range(6):
        plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()
