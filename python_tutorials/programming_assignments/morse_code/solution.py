import argparse
from pathlib import Path


class Morse():
    """
    This class contains the encoding table and functionality to encrypt and
    decrypt morse.
    """
    enc_table = {
        "A": '.-',
        "B": '-...',
        "C": '-.-.',
        "D": '-..',
        "E": '.',
        "F": '..-.',
        "G": '--.',
        "H": '....',
        "I": '..',
        "J": '.---',
        "K": '-.-',
        "L": '.-..',
        "M": '--',
        "N": '-.',
        "O": '---',
        "P": '.--.',
        "Q": '--.-',
        "R": '.-.',
        "S": '...',
        "T": '-',
        "U": '..-',
        "V": '...-',
        "W": '.--',
        "X": '-..-',
        "Y": '-.--',
        "Z": '--..',
        "1": '.----',
        "2": '..---',
        "3": '...--',
        "4": '....-',
        "5": '.....',
        "6": '-....',
        "7": '--...',
        "8": '---..',
        "9": '----.',
        "0": '-----',
        "." : ".-.-.-",
        "," : "--..--",
        ":" : "---...",
        "?" : "..--..",
        "'" : ".----.",
        "-" : "-....-",
        "/" : "-..-.",
        "@" : ".--.-.",
        "=" : "-...-",
        " " : "/"
    }
    dec_table = {v: k for k, v in enc_table.items()}


    def decrypt(input_string):
        """ This function decrypts a given input string using morse. """
        if not input_string:
            return ""

        return "".join([Morse.dec_table[char] for char in input_string.split(" ")])


    def encrypt(input_string):
        """ This function encrypts a given input string using morse. """
        if not input_string:
            return ""

        return " ".join([Morse.enc_table[char] for char in input_string])


def read_file(path_to_file):
    """ Reads the content from a file and replaces newlines with spaces. """
    return path_to_file.read_text().replace("\n", " ")


def write_to_file(path_to_file, text):
    """ Writes text to a file. """
    path_to_file.write_text(text)


def parse_arguments():
    """ Parses user CLI arguments. """
    parser = argparse.ArgumentParser(
        description="decrypts and encrypts morse code"
    )

    parser.add_argument(
        "--src", type=Path, required=True,
        help="path to the file that contains the file to encrypt or decrypt"
    )

    parser.add_argument(
        "--dst", type=Path, required=False, default="output.txt",
        help="path to the file to which to write output"
    )

    parser.add_argument(
        "--encrypt", required=False, default=False, action="store_true",
        help="""indicates that the source file is to be encrypted instead of
                decrypted"""
    )

    return parser.parse_args()


def run():
    """ Entry point. """
    args = parse_arguments()
    file_contents = read_file(args.src)

    if args.encrypt:
        result = Morse.encrypt(file_contents)
    else:
        result = Morse.decrypt(file_contents)

    write_to_file(args.dst, result)


if __name__ == "__main__":
    run()
