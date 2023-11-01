import cv2

def basic_operation():
    img1 = cv2.imread('C:\\Users\\JangBeomJun\\Downloads\\ddd.jpg', cv2.IMREAD_COLOR)
    img2 = img1.copy()
    img3 = img1.copy()

    shape = img1.shape
    size = img1.size
    dtype = img1.dtype

    h = img1.shape[0]

    cv2.putText(img1,'Shape: '+str(shape),(20,h-100),cv2.FONT_HERSHEY_PLAIN,1.5, (255,255,0),2)
    cv2.putText(img1,'Size: '+str(size),(20,h-75),cv2.FONT_HERSHEY_PLAIN,1.5, (255,255,0),2)
    cv2.putText(img1,'Dtype: '+str(dtype),(20,h-50),cv2.FONT_HERSHEY_PLAIN,1.5, (255,255,0),2)

    b,g,r = cv2.split(img2)
    img2 = cv2.merge((r, g, b))
    cv2.imshow('JetsonNano_Basic_Operation_splitNmerge', img2)

    img3[:,:,2] = 0
    cv2.imshow('JetsonNano_Basic_Operation_Channel', img3)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    