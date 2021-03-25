import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", help="Path to the image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# image = cv2.flip(image, 1)
image = cv2.flip(image, 1)

(h, w) = image.shape[:2]
(x, y) = (w//2, h//2)

# To get the rotational matrix we need the point at which it will rotate and the angle
rot = cv2.getRotationMatrix2D((x, y), 45, 1.0)
img = cv2.warpAffine(image, rot, (w, h))

img = cv2.flip(img, 0)
(b, g, r) = img[189, 441]
# cv2.imshow("Original: ", image)

# flipped_hor = cv2.flip(image, 1)
# cv2.imshow("Hor flipped", flipped_hor)

# flipped_ver = cv2.flip(image, 0)
# cv2.imshow("Vertical", flipped_ver)

# flipped_both = cv2.flip(image, -1)
# cv2.imshow("Flipped Both", flipped_both)

print("Blue: ", b)
print("Red", r)
