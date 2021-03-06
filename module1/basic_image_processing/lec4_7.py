import numpy as np
import cv2

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle: ", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle: ", circle)
cv2.waitKey(0)

bitand = cv2.bitwise_and(rectangle, circle)
bitor = cv2.bitwise_or(rectangle, circle)
bitxor = cv2.bitwise_xor(rectangle, circle)
bitnot = cv2.bitwise_not(rectangle, circle)
