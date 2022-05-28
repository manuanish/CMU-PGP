from startup.display_start_page import *
from console.input import *
from utils.clear_terminal import *
from utils.print_space import *
from utils.sanatize_output import *
import os
import subprocess

displayStartPage()

USER_INPUT = None

while True:
    USER_INPUT = input(consoleInput())

    if USER_INPUT[0:3] == "cgp":
        try:
            print(sanatizeOutput(os.popen("gpg" + str(USER_INPUT[3:len(USER_INPUT)])).read()))
        except:
            print("Command failed to run.")

    else:
        try:
            print(sanatizeOutput(os.popen(USER_INPUT)).read())
        except:
            print("Command failed to run.")
