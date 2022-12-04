import cv2
import numpy as np
import os
from pathlib import Path
import template
import solution
import unittest


def read_img(path):
    """ This function read an image from path using opencv. """
    return cv2.imread(path)


class Test(unittest.TestCase):
    def setUp(self):
        self.path_to_images = Path("./images")
        self.path_to_orig = str(self.path_to_images / "landscape.jpg")
        self.orig = read_img(self.path_to_orig)

    def test_read_img(self):
        assert np.array_equal(template.read_img(self.path_to_orig), self.orig)

    def test_invert(self):
        assert np.array_equal(
            template.invert(self.orig),
            solution.invert(self.orig),
        )

    def test_flip_horz(self):
        assert np.array_equal(
            template.flip_horizontally(self.orig),
            solution.flip_horizontally(self.orig),
        )

    def test_flip_vert(self):
        assert np.array_equal(
            template.flip_vertically(self.orig),
            solution.flip_vertically(self.orig),
        )

    def test_to_grayscale(self):
        assert np.array_equal(
            template.to_grayscale(self.orig),
            solution.to_grayscale(self.orig),
        )

    def test_to_black_white(self):
        assert np.array_equal(
            template.to_black_white(self.orig),
            solution.to_black_white(self.orig),
        )

    def test_get_channel(self):
        assert np.array_equal(
            template.get_channel(self.orig, "g"),
            solution.get_channel(self.orig, "g"),
        )

    def test_rotate_nn(self):
        assert np.array_equal(
            template.rotate_nn(self.orig, 45),
            solution.rotate_nn(self.orig, 45),
        )
