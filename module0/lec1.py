import cv2
import argparse
# load our image and convert it to grayscale
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])  # Preferred industrial method

# haerdcoding image = cv2.imread("parthavface.jpeg")

# Converting the image to greyscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=10,
                                  minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
# loop over the faces and draw a rectangle surrounding each
for (x, y, w, h) in rects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
# show the detected faces
cv2.imshow("Faces", image)
cv2.waitKey(0)
