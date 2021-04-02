import cv2
from argparse import ArgumentParser
import numpy as np
import imutils

ap = ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", required=True)
args= vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayclone = gray.copy()
cnts = cv2.findContours(grayclone, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print(cnts)
print(len(cnts))
cv2.imshow("Clone",clone)
cv2.imshow("Original: ", image)
cv2.waitKey(0)