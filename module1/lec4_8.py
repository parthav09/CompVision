import numpy as np
import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Masked: ', masked)
cv2.imshow("Original", mask)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (145, 200), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Masked: ', masked)
cv2.imshow("Original", mask)
cv2.waitKey(0)
