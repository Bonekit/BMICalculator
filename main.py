"""Entry point for the application"""

import tkinter as tk
from lib.GUI import Application

__author__ = "Tobias Menzel"
__copyright__ = "Copyright 2018, BMI-Calculator"
__credits__ = ["Tobias Menzel"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Tobias Menzel"
__email__ = ""
__status__ = "Production"


def main():
    """Main function as starting point"""
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("BMI-Calculator v1.0")
    app.master.maxsize(680, 300)
    app.master.minsize(680, 300)
    app.mainloop()


#   Entry point
if __name__ == "__main__":
    main()
