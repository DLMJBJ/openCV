import cv2
import numpy as np
from matplotlib import pyplot as plt
def image_perspective_transformation():

    img = cv2.imread('C:\\Users\\JangBeomJun\\Desktop\\photo\\a65b87a6a5c139d404f8078432c64390.jpg', cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640, 480))
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])
    pts1 = np.float32([[249, 100], [470, 100], [220, 348], [476, 361]])
    pts2 = np.float32([[10, 10], [1000, 10], [10, 1000], [1000, 1000]])
    cv2.circle(img, (249, 100), 10, (255, 0, 0), -1)
    cv2.circle(img, (470, 100), 10, (0, 255, 0), -1)
    cv2.circle(img, (220, 348), 10, (0, 0, 255), -1)
    cv2.circle(img, (476, 361), 10, (255, 255, 0), -1)
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (1010, 1010))

    plt.subplot(121), plt.imshow(img), plt.title('IMAGE')
    plt.subplot(122), plt.imshow(dst), plt.title('PERSPECTIVE')
    plt.show()