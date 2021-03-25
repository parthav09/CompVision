import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image is required")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Original Image: ", image)

(T, threshInv) = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Yhresh binary inverse: ", threshInv)
(T, thresh) = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh Binary: ", thresh)

cv2.imshow("Masked image", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
