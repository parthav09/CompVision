import cv2
import numpy as np
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path required to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("Original: ", image)

kernelSizes = [(3, 3), (5, 5), (7, 7), (9, 9)]
# Averaging
for (k0, k1) in kernelSizes:
    blurred = cv2.blur(image, (k0, k1))
    cv2.imshow("Average of {} {}".format(k0, k1), blurred)


# Gaussian Blurring
for (k0, k1) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (k0, k1), 0)
    cv2.imshow("Gausian blurred of {} {}".format(k0, k1), blurred)
cv2.destroyAllWindows()

# median BLurring
for k in range(3, 5, 7):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median BLurred: ", blurred)
cv2.waitKey()
