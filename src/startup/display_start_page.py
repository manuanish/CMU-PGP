from startup.logo import *
from utils.center_text import *
from utils.remove_character import *
from utils.print_space import *


def displayStartPage():
    logoFormatted = replace_array(readLogo())
    subtitleFormatted = replace_array(readSubtitle())
    faviconFormatted = replace_array(readFavicon())

    print_space(3)
    print_center_ascii(faviconFormatted, "\033[2m", " " * 8)
    print_space(2)
    print_center_ascii(logoFormatted, "\033[0m" * 2, " ")
    print_space(2)
    print_center_ascii(subtitleFormatted, "\033[2m", " " * 8)
    print_space(5)
    print_center(
        "\033[1mCMU PGP is an encryption program that provides cryptographic privacy and authentication for data communication."
    )
    print_center(
        "This can be used for signing, encrypting, and decrypting texts, e-mails, files, directories, and whole disk partitions and to increase the security of e-mail communications.\033[0m"
    )
    print_space(3)
