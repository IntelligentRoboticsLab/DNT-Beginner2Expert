import sys

if sys.version_info.major != 2:
    print("Please run with python2.7, not python3")
    sys.exit(1)

try:
    import cv2
    print("OpenCV installed correctly")
except ImportError:
    print("OpenCV not installed")

try:
    import naoqi
    print("naoqi installed correctly")
except ImportError:
    print("naoqi not installed")

try:
    import numpy
    print("numpy installed correctly")
except ImportError:
    print("numpy not installed")
    