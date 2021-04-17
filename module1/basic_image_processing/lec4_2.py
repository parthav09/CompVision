import cv2
import numpy
import imutils
from argparse import ArgumentParser

# ap = ArgumentParser()
# ap.add_argument("-i", "--image", help="Path to image", required=True)
# args = vars(ap.parse_args())

# image = cv2.imread(args["image"])
# cv2.imshow("Original image: ", image)

# (h, w) = image.shape[:2]
# (y, x) = (h//2, w//2)

# # The code to rotate the image
# # 1st argument is the point at which u want to rotate, 2. The angle at which you want to rotate
# M = cv2.getRotationMatrix2D((x, y), 45, 1.0)
# # 1. THe image, 2.The rotation, 3.Dimensions always width and height
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotaetd image: ", rotated)

# M = cv2.getRotationMatrix2D((x, y), -90, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated Image: ", rotated)

# rotated_utils = imutils.rotate(image, 180)
# cv2.imshow("Rotated Imutils: ", rotated_utils)
# cv2.waitKey(0)

ap = ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
(y, x) = (h//2, w//2)

M = cv2.getRotationMatrix2D((50, 50), 88, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated: ", rotated)
(b, g, r) = rotated[10, 10]
print("{},{},{}".format(b, g, r))
print(cv2.__version__)
