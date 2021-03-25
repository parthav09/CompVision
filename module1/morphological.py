from argparse import ArgumentParser
import cv2
# construct the argument parser and parse the arguments
i = 0
ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
# apply a series of erosions
# for i in range(7):
#     eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
#     cv2.imshow("Eroded {} times".format(i + 1), eroded)
# cv2.destroyAllWindows()

# # Applying a series of Dilation
# for i in range(0, 7):
#     dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
#     cv2.imshow("Dilated {} times".format(i+1), dilated)

# Applying Opening
kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels and apply an "opening" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(
        kernelSize[0], kernelSize[1]), opening)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)
# loop over the kernels and apply a "closing" operation to the image
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
        kernelSize[0], kernelSize[1]), closing)


for k in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k)
    morphelem = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Morphological: ({} {})".format(k[0], k[1]), morphelem)
cv2.waitKey(0)
