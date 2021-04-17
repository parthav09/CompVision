import numpy as np
import cv2

# Creating a canvas to draw shapes
# canvas = np.zeros((300, 300, 3), dtype="uint8")

# green = (0, 225, 0)
# red = (0, 0, 225)
# blue = (225, 0, 0)

# cv2.line(canvas, (0,0), (300,300), green)
# cv2.imshow("Canvas Green: ", canvas)


# cv2.line(canvas, (300, 0), (0, 300), red, 3) #(image, start point, end point, color , thickness)
# cv2.imshow("Canvas Red: ", canvas)

# cv2.rectangle(canvas, (10,10), (60,60), green)
# cv2.imshow("Canvas", canvas)

# cv2.rectangle(canvas, (50,120), (100,225), red, -1)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)


# Drawing a circle
canvas = np.zeros((300, 300, 3), dtype="uint8")
white = (225, 225, 225)
(h, w) = canvas.shape[:2]
y = h//2
x = w//2
# (x, y) = (canvas.shape[1]//2, canvas.shape[0]//2)

for r in range(0, 175, 25):
    # Takes the center as the second argiment and the third argumet is the radius
    cv2.circle(canvas, (x, y), r, white)
cv2.imshow("Canvas Circle:", canvas)
cv2.waitKey(0)
