#!/usr/bin/env python2

import cv2
import glob
import numpy as np
import os

from naoqi import ALProxy


# Robot name as shown on its head followed by .local
IP = "EVE.local"
PORT = 9559


# For this assignment you will have three ways of testing your code.
# 1. Test your code on the images in the folder "imgs".
# 2. Test your code on the webcam.
# 3. Test your code on the robot.

# It is best to start with the images as you can run your code without needing a robot.
# If you get your code to work on the images, you can implement the functions for the webcam and and the robot.
# In the main function you can make it so that you can switch between the different camera types depending on the value of CAMERA_TYPE.

# 0: images from folder, 1: webcam, 2: robot
CAMERA_TYPE = 0

def read_imgs(img_dir):
    '''
    Read images from the given folder and return them in a list.
    https://www.quora.com/How-can-I-read-multiple-images-in-Python-presented-in-a-folder

    Input:      path to the folder containing the images
    Output:     list of images
    '''
    pass
    return imgs


def mask_img(img):
    '''
    Create a binary image in which orange is white and the rest is black.
    https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

    Input:      image in RGB
    Output:     binary image
    '''
    pass
    return mask


def detect_circles(img):
    '''
    Detect circles in a binary image.
    returns the centre coordinates and the radius of the ball in the image.
    https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/

    Input:      binary image
    Output:     centre coordinates and radius of the ball (x, y, r)
    '''
    pass
    return x, y, r


def detect_orange_ball(img):
    '''
    Detect an orange ball in the given image.
    returns the centre coordinates and the radius of the ball in the image.

    Input:      image in RGB
    Output:     centre coordinates and radius of the ball (x, y, r)
    '''
    pass
    return x, y, r


# Once you have implemented the functions for the orange ball detection and have it working on the images, 
# you can test it on the webcam and the robot by implementing the following functions:

def start_webcam():
    '''
    Start the webcam and return the capture device.
    https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
    '''
    pass
    return cap


def get_img_from_webcam(cap):
    '''
    Get a frame from the webcam and return it.
    https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
    '''
    pass
    return frame


def close_webcam(cap):
    '''
    Stop the connection with the webcam.
    https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
    '''
    pass


def create_video_connection(ip=None, port=None, camera=0):
    '''
    Create a connection with the robot and start a camera proxy.
    returns the video device and the capture device.
    https://gist.github.com/takamin/990aa0133919aa58944d
    '''
    if ip == None: ip = IP
    if port == None: port = PORT
    pass
    return video_device, capture_device


def get_img_from_robot(video_device, capture_device):
    '''
    Get a frame from the robot and return it as numpy array.
    https://gist.github.com/takamin/990aa0133919aa58944d
    '''
    # Create image
    pass
    return img


# From this function your program will start
# Use it to test your code after completing each function to make sure it works.
# When you know that your code works, you can combine them in the main function.

# After everything works with the images, you can test it on the webcam and the robot.
# Use the CAMERA_TYPE variable to switch between the different camera types.

def main():
    # Depending on the camera type (folder, webcam, robot)
    # Loop over the images, detect the ball and show the results
    print("Good luck")



if __name__ == "__main__":
    main()
