import cv2


def main() :
    img = cv2.imread('C:\\Users\\JangBeomJun\\Downloads\\photo-1595126739121-68ab4225f9cf.jpg',cv2.IMREAD_COLOR)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('original',img)
    cv2.imshow('gray',gray_img)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()