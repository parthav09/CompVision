import cv2
import numpy
import imutils
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image",
                help="Path to the image is required", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("original", image)

# the ration where 150 is new height and dividing it by the old height to get the ratio
r = 150/image.shape[0]
dim = (int(image.shape[1]*r), 150)


resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

resized_utils = imutils.resize(image, width=100)
cv2.imshow("Resized_Imutils", resized_utils)

cv2.imshow("Resized:", resized)
cv2.waitKey()
# import argparse
# import imutils
# import cv2
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(ap.parse_args())
# # load the image and show it
# image = cv2.imread(args["image"])
# cv2.imshow("Original", image)
# # we need to keep in mind aspect ratio so the image does not look skewed
# # or distorted -- therefore, we calculate the ratio of the new image to
# # the old image. Let's make our new image have a width of 150 pixels
# r = 150.0 / image.shape[1]
# dim = (150, int(image.shape[0] * r))
# # perform the actual resizing of the image
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized (Width)", resized)
# cv2.waitKey()
