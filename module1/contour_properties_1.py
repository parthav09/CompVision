import cv2
from argparse import ArgumentParser
import imutils

ap = ArgumentParser()
ap.add_argument("-i", "--image", help = "Path to the image is required", required =True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
for c in cnts:
    M = cv2.moments(c)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.circle(clone, (cx, cy), 10, (0, 255, 0), -1)
cv2.imshow("Centroids", clone)


cv2.imshow("Original: ", image)
cv2.waitKey()