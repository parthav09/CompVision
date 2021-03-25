import numpy as np
import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# Using cv2 ka add function
print("Max of 255 is {}".format(
    str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("Min of 0 is {}".format(
    str(cv2.subtract(np.uint8([200]), np.uint8([100])))))

# Using NumPy arithmetic operations
print("Wrap aroung addition: {}".format(
    str(np.uint8([200]) + np.uint8([100]))))
print("Wrap aroung subtraction: {}".format(
    str(np.uint8([200]) - np.uint8([100]))))

# Increasing the pixel size by 100
M = np.ones(image.shape, dtype="uint8")*100
added = cv2.add(image, M)
cv2.imshow(added)

N = np.ones(image.shape, dtype="uint8")*50
subtract = cv2.subtract(image, N)
cv2.imshow("Subtract: ", subtract)

cv2.imshow("Original", image)
cv2.waitKey(0)
