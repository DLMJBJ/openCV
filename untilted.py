import cv2
import numpy as np

def line() :
    img  = np.zeros((512,512,3), np.uint8)
    img.fill(255)
    img = cv2.line(img, (300,0), (100,511),(0,255,0),5)
    cv2.imshow('fs',img)
    cv2.waitKey(0)
    cv2.destroyWindow()

def rectangle() :
    img  = np.zeros((512,512,3), np.uint8)
    img.fill(255)
    img = cv2.rectangle(img, (100,150), (500,300),(0,255,0),5)
    cv2.imshow('fs',img)
    cv2.waitKey(0)
    cv2.destroyWindow()

def circle():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(255)
    img = cv2.circle(img, (300, 200), 100, (0, 255, 0), 40)
    cv2.imshow('sdf', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ellipse():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(255)
    img = cv2.ellipse(img, (256, 256), (120, 50), 320, 0, 315, (0, 255, 0), -1)
    cv2.imshow('dsf', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def text():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(255)
    img = cv2.putText(img, 'HELLO', (100, 400), cv2.FONT_HERSHEY_PLAIN, 6, (0, 180, 256), 5)
    cv2.imshow('JetsonNano_PutText', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def all():
    img  = np.zeros((512,512,3), np.uint8)
    img.fill(255)

    img = cv2.line(img, (300,0), (100,511),(255,0,0),5)
    img = cv2.rectangle(img, (300,120), (40,40),(0,255,0),1)
    img = cv2.circle(img, (300, 200), 100, (0, 255, 0), 10)
    img = cv2.ellipse(img, (400, 400), (30, 30), 0, 0, 270, (0, 0, 255), -1)
    img = cv2.putText(img, 'HELLO', (100, 400), cv2.FONT_HERSHEY_PLAIN, 6, (0, 180, 256), 5)
    cv2.imshow('dsf', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    