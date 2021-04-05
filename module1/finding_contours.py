import cv2
from argparse import ArgumentParser
import numpy as np
import imutils

ap = ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", required=True)
args= vars(ap.parse_args())

image = cv2.imread(args["image"])
# clone = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayclone = gray.copy()
cnts = cv2.findContours(grayclone, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print(cnts)
print(len(cnts))
# cv2.imshow("Clone",clone)
#finding drawing contours
clone = image.copy()
for (i, c) in enumerate(cnts):
	print("Drawing contour #{}".format(i + 1))
	cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Single Contour", clone)
clone = image.copy()
cv2.destroyAllWindows()
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Slice", clone)

clone = image.copy()
cv2.destroyAllWindows()
for c in cnts:
    mask = np.zeros(gray.shape, dtype="uint8")
    cv2.drawContours(clone, [c], -1, (0, 255, 0), 2)
    cv2.imshow("Image", image)
    cv2.imshow("Mask", mask)
    cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
cv2.waitKey(0)
# cv2.imshow("Original: ", image)
# cv2.waitKey(0)