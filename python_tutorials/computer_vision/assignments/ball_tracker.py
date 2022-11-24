#!/usr/bin/env python2

# Check if python is version 2.7
import sys
if sys.version_info.major != 2:
    print("Please run with python2.7, not python3")
    sys.exit(1)

# Import libraries that will likely be used
try:
    import cv2
    import itertools
    import numpy as np

    from naoqi import ALProxy

except ImportError:
    print("Error when importing libraries. Please run the install_test.py script in the computer_vision folder.")
    sys.exit(1)

# Import self written functions from orange_ball.py

from orange_ball import create_video_connection, get_img_from_robot, detect_orange_ball

from kick import kick

# Robot name as shown on its head followed by .local
# TODO: Change this to your robots name when testing on the robot
IP = "EVE.local"
PORT = 9559

if IP == "EVE.local":
    print("Please change the IP variable in the code to your robots name.")
    sys.exit(1)

# Tracking method: 0: head, 1: walk to ball, 2: kick ball
TRACKING_METHOD = 0

def start_proxies():
    '''
    Start the motion, posture and memory proxy and let the robot stand up.
    '''
    pass
    return motion_proxy, posture_proxy, memory_proxy


def track_ball_with_head(motion_proxy, x, y, width, height):
    '''
    Track the ball with the robots head by changing the head yaw and pitch.

    x: x position of the centre of the ball in the image.
    y: y position of the centre of the ball in the image.
    width: width of the image.
    height: height of the image.
    http://doc.aldebaran.com/2-8/naoqi/motion/control-joint-api.html#ALMotionProxy::changeAngles__AL::ALValueCR.AL::ALValueCR.floatCR
    '''
    # Move head left or right depending on the x position of the ball (HeadYaw)
    # Move head up or down depending on the y position of the ball (HeadPitch)
    pass


def reset_head_to_centre(motion_proxy):
    '''
    Reset the head angles to zero.
    http://doc.aldebaran.com/2-8/family/nao_technical/joints_naov6.html
    '''
    motion_proxy.setAngles("HeadYaw", 0, 0.1)
    motion_proxy.setAngles("HeadPitch", 0, 0.1)


def move_to_ball(motion_proxy, x, y, width, height):
    '''
    Move towards the ball.

    x: x position of the centre of the ball in the image.
    y: y position of the centre of the ball in the image.
    width: width of the image.
    height: height of the image.
    http://doc.aldebaran.com/2-8/naoqi/motion/control-walk-api.html#ALMotionProxy::moveToward__floatCR.floatCR.floatCR
    '''
    # Turn towards the ball if not in the centre of the image
    # Walk towards the ball (moveToward)
    pass


def kick_ball(motion_proxy, posture_proxy, x, width):
    '''
    Kick the ball if the ball is close enough.
    '''
    # Stop the current movement of the robot
    # Go to the standInit position
    # Kick with the correct leg
    # Go to the standInit position
    pass

def search_for_ball(motion_proxy):
    '''
    Search for the ball by moving the robots head.
    '''
    pass


def main():
    # Start connections with the robot
    # Obtain image from the robot and detect the ball
    # Depending on TRACKING_METHOD, track the ball with the robots head
    # or by walking towards the ball
    # Search for the ball if no ball is found
    pass
    # Let the robot sit when done
    motion_proxy.stopMove()
    motion_proxy.rest()


if __name__ == "__main__":
    main()
