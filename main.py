import cv2

image1 = cv2.imread("/Users/admin/python-imagefilter-groupe_7/images/armin.png")
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original images', image1)
cv2.imshow('Gray images', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


