# Title                 : BMI-Calculator
# Description           : BMI-Calculator v1.0
# Author                : Tobias Menzel
# Date                  : 10.09.2018
# Notes                 :
# Python_version        : 3.6.6
# ==========================================================================================

# Import Modules for the BMI-Calculator. 
import subprocess
import re
import datetime
import time
import tkinter as tk
import os
from lib.GUI import Application


# ===============================
#         MAIN FUNCTIONS
# ===============================

# Main Function.


def main():
    # GUI Entry Point.
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

    # # User Input to get weight and size.
    # weight = input('Please enter your weight in kg: ')
    # if not re.match(r'\d', weight):
    #     print('Use only numbers!')
    #     return
    # else:
    #     weight = int(weight)
    #
    # size = input('Please enter your size in m: ')
    # if not re.match(r'\d\.', size):
    #     print('Use only numbers and one dot, like this example: "1.90"')
    #     return
    # else:
    #     size = float(size)


# ===============================
#         MAIN PROGRAM
# ===============================


#   Main Program.
if __name__ == "__main__":
    #   Launch main menu.
    main()
