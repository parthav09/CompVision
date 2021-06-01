#importing all the required libraries

from pysearchimage.object_detection.helpers import sliding_window
from pysearchimage.object_detection.helpers import pyramid
import time
import cv2
from argparse import ArgumentParser

ap = ArgumentParser()
ap.add_argument("-i", "--image", help = "Path to the image is required", required= True)
ap.add_argument("-w", "--width", path = "Path to the image is required", required= True)
ap.add_argument("-h", "--height",path = "Path to the image is required", required= True)
ap.add_argument("-s", "--scale", path = "Path to the image is required", required= True)

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
(winW, winH) = (args['width'], args['height'])