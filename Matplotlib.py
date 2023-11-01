import cv2
from matplotlib import pyplot as plt

def matplotlib():
    img = cv2.imread("C:\\Users\\JangBeomJun\\Downloads\\photo-1595126739121-68ab4225f9cf.jpg",cv2.IMREAD_COLOR)

    fig = plt.figure()
    #fig.canvas.set_windows_title('JetsonNano_Matplot')
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()

    fig = plt.figure()
    #fig.canvas.set_windows_title('JetsonNano_Matplot')
    b,g,r = cv2.split(img)
    img2 = cv2.merge([r,g,b])
    plt.imshow(img2)
    plt.xticks([])
    plt.yticks([])
    plt.show()