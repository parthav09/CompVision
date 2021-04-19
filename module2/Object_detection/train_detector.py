from __future__ import print_function
from imutils import paths
from scipy.io import loadmat
from skimage import io
from argparse import ArgumentParser
import dlib
import sys

if sys.version_info > (3,):
    long = int

ap = ArgumentParser()
ap.add_argument("-c", "--class", required=True,
	help="Path to the CALTECH-101 class images")
ap.add_argument("-a", "--annotations", required=True,
	help="Path to the CALTECH-101 class annotations")
ap.add_argument("-o", "--output", required=True,
	help="Path to the output detector")
args = vars(ap.parse_args())