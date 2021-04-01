import cv2
import imutils
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image is required")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)

wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)
auto = imutils.auto_canny(blurred)

cv2.imshow("Wide", wide)
cv2.imshow("Tight", tight)
cv2.imshow("Auto", auto)

cv2.imshow("Original: ", image)
cv2.waitKey(0)