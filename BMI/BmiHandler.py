# ===============================
#       BMI HANDLER Class
# ===============================

# Import Modules for BmiHandler Class.
import csv
import time
import os

# BmiHandler Class.


class BmiHandler:
    def __init__(self, weight, size, folder):
        self.__weight = weight
        self.__size = size
        self._folder = folder
        self._file = 'history.csv'

    def bmi_calculator(self):
        """Calculate the BMI-Index"""
        return round(self.__weight / self.__size ** 2, 1)

    def bmi_message(self, bmi_value):
        pass

    def bmi_to_csv(self, history):
        """Write Data to a .csv file, encoded in UTF-8
        - Data: date, weight, size, BMI.
        """
        with open(os.path.join(self._folder, self._file), 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(history)

    def bmi_compare(self, bmi_value):
        """Compare the old bmi-index with the new one"""
        try:
            with open(os.path.join(self._folder, self._file), 'r', encoding='UTF-8', newline='') as file:
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