"""Entry point for the application"""

import tkinter as tk
from lib.GUI import Application

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
