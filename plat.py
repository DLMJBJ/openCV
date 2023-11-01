import cv2

def image_RSW():
    fName = 'C:\\Users\\JangBeomJun\\Downloads\\photo-1595126739121-68ab4225f9cf.jpg'
    
    orginal = cv2.imread(fName,cv2.IMREAD_COLOR)
    cv2.imshow('JetsonNano_Original', orginal)
    
    gray = cv2.imread(fName, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('JetsonNano_Gray', gray)
    
    unChange = cv2.imread(fName, cv2.IMREAD_UNCHANGED)
    cv2.imshow('JetsonNano_Unchanged', unChange)
    
    cv2.imwrite('GRAYIMAGE.png',gray);
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

