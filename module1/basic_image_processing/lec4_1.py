import numpy as np
import cv2
from argparse import ArgumentParser
import imutils

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path is required")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original: ", image)


W = np.float32([[1, 0, 25], [0, 1, 25]])
shifted = cv2.warpAffine(image, W, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted: ", shifted)

# we can do the same thing using imutils
# import numpy as np
# import cv2
# def translate(image, x, y):
# 	# define the translation matrix and perform the translation
# 	M = np.float32([[1, 0, x], [0, 1, y]])
# 	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# 	# return the translated image
# 	return shifted

shifted = imutils.translate(image, 10, 10)
cv2.imshow("Imutils shifted: ", shifted)
cv2.waitKey(0)
