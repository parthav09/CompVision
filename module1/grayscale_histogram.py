import matplotlib.pyplot as plt
import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required = True, help="Path to the image is required")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# construct a grayscale histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# matplotlib expects RGB images so convert and then display the image
# with matplotlib to avoid GUI conflicts/errors (mainly on macOS)
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB))
# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.ylim([0, 4000])
plt.xlim([0, 256])
plt.show()