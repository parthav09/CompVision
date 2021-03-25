import argparse
import cv2

# construct the argument parser and parse arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())# "--image" is a switch/string that we specify at the command line this tell our .py script where the imge is saved on our disk.

image = cv2.imread(args["image"])
# image = cv2.imread("Path/to/image")
print("Width: {} pixels".format(image.shape[1]))
print("Height: {} pixels".format(image.shape[0]))
print("Channel: {} pixels".format(image.shape[2]))

cv2.imshow()
cv2.waitKey(0)
