import argparse
import cv2
import numpy as np
from pathlib import Path


def read_img(path):
    """ This function read an image from path using opencv. """
    return cv2.imread(path)


def save_img(img, path):
    """ This function stores an image to path using opencv. """
    cv2.imwrite(path, img)


def invert(img):
    """ This function takes an image as input and inverts it. """
    return 255 - img


def flip_horizontally(img):
    """ This function takes an image as input and flips it horizontally. """
    return np.flip(img, axis=0)


def flip_vertically(img):
    """ This function takes an image as input and flips it vertically. """
    return np.flip(img, axis=1)


def to_grayscale(img):
    """ This function takes an image as input and converts it to grayscale. """
    return np.sum(img, axis=2) * 0.33


def to_black_white(img):
    """
    This function takes an image as input and uses a thresh hold to make it
    black and white.
    """
    return cv2.threshold(to_grayscale(img), 128, 255, cv2.THRESH_BINARY_INV)[1]


def get_channel(img, c):
    """
    This function takes an image as input and either "b", "g" or "r". It returns
    only values in the corresponding channel.
    """
    i = ["b", "g", "r"].index(c) 
    res = np.zeros(img.shape)
    res[:, :, i] = img[:, :, i]
    return res


def rotate_nn(img, deg):
    """
    This function takes an image as input and rotates it by x degrees using
    nearest neighbour interpolation.
    """
    angle = deg * np.pi / 180.0 
    res = np.zeros(img.shape)

    center_row = img.shape[0] // 2
    center_col = img.shape[1] // 2

    row_coord = np.arange(img.shape[0])[:, None] - center_row
    col_coord = np.arange(img.shape[1]) - center_col

    source_row = row_coord * np.cos(angle) - col_coord * np.sin(angle) + center_row
    source_col = row_coord * np.sin(angle) + col_coord * np.cos(angle) + center_col
    
    mask = (source_row >= 0) & (source_row < img.shape[0] - 1) & (source_col >= 0) & (source_col < img.shape[1] - 1)
    res[mask] = img[source_row[mask].round().astype(int), source_col[mask].round().astype(int)]

    return res


def parse_arguments():
    """ This function parses CLI arguments. """
    parser = argparse.ArgumentParser(
        description="manipulates images"
    )

    parser.add_argument(
        "--src", type=Path, required=True,
        help="path to the file that contains the image to manipulate"
    )

    parser.add_argument(
        "--dst", type=Path, required=False, default="output.jpeg",
        help="path to which to write the output"
    )
    
    parser.add_argument(
        "--invert", required=False, default=False, action="store_true",
        help="inverts the image"
    )
    
    parser.add_argument(
        "--flip-horz", required=False, default=False, action="store_true",
        help="flips the image horizontally"
    )
    
    parser.add_argument(
        "--flip-vert", required=False, default=False, action="store_true",
        help="flips the image vertically"
    )

    parser.add_argument(
        "--grayscale", required=False, default=False, action="store_true",
        help="""makes the image grayscale"""
    )

    parser.add_argument(
        "--bw", required=False, default=False, action="store_true",
        help="makes the image black white"
    )
    
    parser.add_argument(
        "--channel", required=False, default=None,
        help="gets a specific channel, either g, b or r"
    )

    parser.add_argument(
        "--rotate", type=int, required=False, default=0,
        help="rotates the image by x degrees"
    )

    return parser.parse_args()


def run():
    """ Entry point. """
    args = parse_arguments()
    print(args)
    res = read_img(str(args.src))

    if args.invert:
        res = invert(res)

    if args.flip_horz:
        res = flip_horizontally(res)

    if args.flip_vert:
        res = flip_vertically(res)

    if args.grayscale:
        res = to_grayscale(res)

    if args.bw:
        res = to_black_white(res)

    if args.channel:
        res = get_channel(res, args.channel)
    
    if args.rotate:
        res = rotate_nn(res, args.rotate)

    save_img(res, str(args.dst))


if __name__ == "__main__":
    run()
