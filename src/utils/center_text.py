import shutil


def print_center(s):
    print(s.center(shutil.get_terminal_size().columns))


def print_center_ascii(s, color, offset):
    for i in s:
        print(
            (offset + color + i + "\033[0m").center(shutil.get_terminal_size().columns)
        )
