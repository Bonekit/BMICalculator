# Title                 : BMI-Calculator
# Description           : BMI-Calculator v1.0
# Author                : Tobias Menzel
# Date                  : 10.09.2018
# Notes                 :
# Python_version        : 3.7.1
# ==========================================================================================

# Import modules
import tkinter as tk
from lib.GUI import Application


# ===============================
#         MAIN FUNCTION
# ===============================

# Main Function


def main():
    # GUI Entry Point.
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("BMI-Calculator v1.0")
    app.master.maxsize(1000, 400)
    app.mainloop()


# ===============================
#         MAIN PROGRAM
# ===============================


#   Entry point
if __name__ == "__main__":
    main()
