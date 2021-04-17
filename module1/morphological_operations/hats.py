import cv2
import numpy as np
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# applying the blackhat operation which finds darker images in lighter background
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
# applying tophat to find laight images in darker background
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Blackhat: ", blackhat)
cv2.imshow("Tophat: ", tophat)

cv2.waitKey()
