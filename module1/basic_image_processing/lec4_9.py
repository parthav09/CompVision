import numpy as np
import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image is required")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
(b, g, r) = cv2.split(image)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)

merged = cv2.merge([b, g, r])
cv2.imshow("Merged", merged)
cv2.waitKey()
cv2.destroyAllWindows()
