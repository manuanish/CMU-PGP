import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def readLogo():
    return tuple(open(ROOT_DIR + "/images/logo.txt", "r"))


def readFavicon():
    return tuple(open(ROOT_DIR + "/images/favicon.txt", "r"))


def readSubtitle():
    return tuple(open(ROOT_DIR + "/images/subtitle.txt", "r"))
