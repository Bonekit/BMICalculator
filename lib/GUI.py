# Title:            GUI Class
# Description:      GUI Class created with Tkinter
# Author:           Tobias Menzel
# Date:             26.10.2018
# Language:         Python 3.7.1 & Tkinter
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import modules required for the GUI class.
import csv
import os
import tkinter as tk
import time
from datetime import datetime


class Application(tk.Frame):
    """A Tkinter gui class"""

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Initiate default values.
        self.file_name = 'history.csv'
        self.file_path = os.getenv('USERPROFILE')
        self.calc_date = '{:%B %d, %Y}'.format(datetime.now())

        # Add Label and entry field for the firstname.
        self.lbl_firstname = tk.Label(self)
        self.lbl_firstname['text'] = "Please enter your firstname:"
        self.lbl_firstname.pack(side="top", anchor="nw")
        self.firstnameEntry = tk.Entry(self)
        self.firstnameEntry.pack()
        self.firstname = tk.StringVar()

        # Add Label and entry field for the lastname.
        self.lbl_lastname = tk.Label(self)
        self.lbl_lastname['text'] = "Please enter your lastname:"
        self.lbl_lastname.pack(side="top", anchor="nw")
        self.lastnameEntry = tk.Entry(self)
        self.lastnameEntry.pack()
        self.lastname = tk.StringVar()

        # Add Label and entry field for the weight.
        self.lbl_weight = tk.Label(self)
        self.lbl_weight['text'] = "Please enter your weight:"
        self.lbl_weight.pack(side="top", anchor="nw")
        self.weightEntry = tk.Entry(self)
        self.weightEntry.pack()
        self.weight = tk.StringVar()

        # Add Label and entry field for the height.
        self.lbl_height = tk.Label(self)
        self.lbl_height['text'] = "Please enter your height:"
        self.lbl_height.pack(side="top", anchor="nw")
        self.heightEntry = tk.Entry(self)
        self.heightEntry.pack()
        self.height = tk.StringVar()

        # Add message field
        self.lbl_msg = tk.Label(self)
        self.lbl_msg['text'] = "Message Box:"
        self.lbl_msg.pack(side="top", anchor="nw")
        self.txt_msg = tk.Text(self, height=5)
        self.txt_msg.pack(side="top", fill="both")

        # Add button to start calculation.
        self.btn_calculate = tk.Button(self, height=1, width=10)
        self.btn_calculate["text"] = "Calculate"
        self.btn_calculate["command"] = self.execute
        self.btn_calculate.pack(side="left", padx=2, pady=2)

        # Add button to exit application.
        self.btn_quit = tk.Button(self, height=1, width=10)
        self.btn_quit["text"] = "Exit"
        self.btn_quit["command"] = self.quit
        self.btn_quit.pack(side="right", padx=2, pady=2)

    def execute(self):
        """Execute calculation and save the data into a csv file"""
        # Get values
        self.height = self.heightEntry.get()
        self.weight = self.weightEntry.get()
        self.firstname = self.firstnameEntry.get()
        self.lastname = self.lastnameEntry.get()

        # Get the calculated bmi.
        bmi = self.calculate(self.height, self.weight)

        # Save the data into a csv file.
        self.save_to_csv(self.height, self.weight, bmi)

        # Compare the old bmi with the new one.
        self.compare(bmi)

        # Clean up entry fields.
        self.clean_up()

    def calculate(self, height, weight):
        """Calculate the BMI-Index"""
        # Cast the values into float.
        hi = float(height)
        we = float(weight)

        # Calculate
        self.txt_msg.insert('end', str(round(we / (hi ** 2), 1)))

        # Return
        return str(round(we / (hi ** 2), 1))

    def save_to_csv(self, height, weight, bmi):
        """Write Data to a .csv file, encoded in UTF-8"""
        # Add data to list.
        history = [self.calc_date, weight, height, bmi]

        # Save data to csv.
        with open(os.path.join(self.file_path, self.file_name), 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(history)

    def compare(self, bmi):
        """Compare the old bmi-index with the new one"""
        try:
            with open(os.path.join(self.file_path, self.file_name), 'r', encoding='UTF-8', newline='') as file:
                reader = csv.reader(file)
                lines = [row for row in reader]
                for line in lines[-1:]:
                    if float(bmi) <= float(line[3]):
                        print('Same Weight or less, good!')
                        print('Old BMI: {}, new BMI: {}\n'.format(str(line[3]), str(bmi)))
                    else:
                        print('You gained Weight, don´t eat so much food!')
                        print('Old BMI: {}, new BMI: {}\n'.format(str(line[3]), str(bmi)))
        except FileNotFoundError:
            print('Nothing to compare, this seems to be your first entry.')
        time.sleep(1)

    def clean_up(self):
        """Clean up textboxes"""
