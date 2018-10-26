# Title:            GUI Class
# Description:      GUI Class created with Tkinter
# Author:           Tobias Menzel
# Date:             26.10.2018
# Version:
# Language:         Python 3.6 & Tkinter
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# Import modules required for the GUI class.
import csv
import os
import tkinter as tk
import time
from datetime import datetime


# Define GUI Class.


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Initiate default values.
        self.file_name = 'history.csv'
        self.file_path = os.getenv('HOME')
        self.calc_date = '{:%B %d, %Y}'.format(datetime.now())

        # Add button to start calculation.
        self.btn_calculate = tk.Button(self)
        self.btn_calculate["text"] = "Calculate"
        self.btn_calculate["command"] = self.calculate
        self.btn_calculate.pack(side="top")

        # Add button to exit application.
        self.btn_quit = tk.Button(self)
        self.btn_quit["text"] = "Exit"
        self.btn_quit["command"] = self.master.destroy
        self.btn_quit.pack(side="bottom")

    def calculate(self):
        """Calculate the BMI-Index"""
        # Declaration.
        size = 0.0
        weight = 0.0
        value = 0.0

        # Calculate.
        value = round(size / weight ** 2, 1)

    def save_to_csv(self):
        """Write Data to a .csv file, encoded in UTF-8
        - Data: date, weight, size, BMI.
        """
        # Declaration.
        weight = ""
        size = 0.0
        bmi_value = 0.0

        # Add data to list.
        history = [self.calc_date, weight, size, bmi_value]

        # Save data to csv.
        with open(os.path.join(self.file_path, self.file_name), 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(history)

    def compare(self, bmi_value):
        """Compare the old bmi-index with the new one"""
        try:
            with open(os.path.join(self.file_path, self.file_name), 'r', encoding='UTF-8', newline='') as file:
                reader = csv.reader(file)
                lines = [row for row in reader]
                for line in lines[-1:]:
                    if float(bmi_value) <= float(line[3]):
                        print('Same Weight or less, good!')
                        print('Old BMI: {}, new BMI: {}\n'.format(str(line[3]), str(bmi_value)))
                    else:
                        print('You gained Weight, don´t eat so much food!')
                        print('Old BMI: {}, new BMI: {}\n'.format(str(line[3]), str(bmi_value)))
        except FileNotFoundError:
            print('Nothing to compare, this seems to be your first entry.')
        time.sleep(1)
