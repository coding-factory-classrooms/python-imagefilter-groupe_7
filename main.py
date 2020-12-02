import cv2


def gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original images', image1)
    cv2.imshow('Gray images', gray)
    
    return gray



image1 = cv2.imread("/Users/admin/python-imagefilter-groupe_7/images/armin.png")
image2 = cv2.imread("/Users/admin/python-imagefilter-groupe_7/images/thesaitama.png")






cv2.imwrite("/Users/admin/python-imagefilter-groupe_7/images2.0/armin.png", gray)



