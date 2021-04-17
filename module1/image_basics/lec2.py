import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image is required")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]

(b, g, r) = image[111, 225]  # top left corner
print("Blue: {b},  Green: {g},  Red: {r}".format(b=b, g=g, r=r))

# turning the top left pixel red
image[0, 0] = (0, 0, 225)
(b, g, r) = image[0, 0]
print("Blue: {b},  Green: {g},  Red: {r}".format(b=b, g=g, r=r))

# lets grab a particular part of the image
# as we know height = h, and width = w

(x, y) = (w//2, h//2)
topleft = image[0:y, 0:x]
topright = image[0:y, x:w]

bottomleft = image[y:h, 0:x]
bottomright = image[y:h, x:w]

cv2.imshow("top left", topleft)
cv2.imshow("top right", topright)
cv2.imshow("bottom left", bottomleft)
cv2.imshow("bottom right", bottomright)

image[0:y, 0:x] = (0, 225, 0)
cv2.imshow("Green Screen", image)
cv2.waitKey(0)
