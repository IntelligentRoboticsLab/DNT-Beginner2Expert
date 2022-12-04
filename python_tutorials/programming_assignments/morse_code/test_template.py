import os
from pathlib import Path
import unittest

from template import Morse


path_to_ciphers = Path("./ciphers")
path_to_plaintexts = Path("./plaintexts")


def read_file(path_to_file):
    return path_to_file.read_text().replace("\n", "")


class TestDecryption(unittest.TestCase):
    def test_decryption(self):
        files = os.listdir(path_to_ciphers)
        for file in files:
            i = read_file(path_to_ciphers / file)
            o = read_file(path_to_plaintexts / file)

            assert Morse.decrypt(i) == o

class TestEncryption(unittest.TestCase):
    def test_encryption(self):
        files = os.listdir(path_to_ciphers)
        for file in files:
            i = read_file(path_to_plaintexts / file)
            o = read_file(path_to_ciphers / file)

            assert Morse.encrypt(i) == o
