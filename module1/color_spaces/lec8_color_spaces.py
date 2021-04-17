# import the necessary packages
from argparse import ArgumentParser
import cv2

# construct the argument parser and parse the arguments
ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the original image and display it (RGB)
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
    cv2.imshow(name, chan)

# Checking for HSV Color spaces
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, chan)

# checking for LAB Color spaces
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
for (name, chan) in zip(("L", "a", "b"), cv2.split(lab)):
    cv2.imshow(name, chan)

# wait for a keypress, then close all open windows
cv2.waitKey(0)
cv2.destroyAllWindows()
