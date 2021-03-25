import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)

# apply Otsu's automatic thresholding -- Otsu's method automatically
# determines the best threshold value `T` for us
#here 0 acts as a dont care parameter as in otsu the T is automatically computed
(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
print("Threshhold value is {}".format(T))
cv2.imshow("THreshhold image ", cv2.bitwise_and(image, image, mask=threshInv))


cv2.imshow("Original: ", image)
cv2.waitKey(0)
