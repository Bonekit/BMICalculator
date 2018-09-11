# Title                 : BMI-Calculator
# Description           : BMI-Calculator v1.0
# Author                : Tobias Menzel
# Date                  : 10.09.2018
# Notes                 :
# Python_version        : 3.6.6
# ==========================================================================================

# Import Modules for the BMI-Calculator. 
import subprocess
import csv
import re
import datetime
import time

# ===============================
#       MAIN FUNCTIONS
# ===============================

# Calculator to calculate the bmi.


def bmi_calculator(weight, size):
    """Calculate the BMI-Index"""
    return weight / size **2


def bmi_to_csv(history):
    """Write Data to a .csv file, encoded in UTF-8
    - Data: date, weight, size, BMI.
    """
    with open('./output/history.csv', 'a', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(history)


def bmi_compare(bmi):
    """Compare the old bmi-index with the new one"""
    try:
        with open('./output/history.csv', 'r', encoding='UTF-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if float(bmi) <= float(row[3]):
                    print('Same Weight or less, good!')
                    print('Old BMI: {}, new BMI: {}\n'.format(str(row[3]), str(bmi)))
                else:
                    print('You gained Weight, don´t eat so much food!')
                    print('Old BMI: {}, new BMI: {}\n'.format(str(row[3]), str(bmi)))
    except FileNotFoundError:
        print('Nothing to compare, this seems to be your first entry.')
    time.sleep(1)

# Main Function to calculate the bmi.


def main():
    # Welcome.
    subprocess.call('cls', shell=True)
    print('Welcome to the BMI-Calculator v1.0')

    # User Input to get weight and size.
    weight = input('Please enter your weight in kg: ')
    if not re.match(r'\d', weight):
        print('Use only numbers!')
        return
    else:
        weight = int(weight)

    # TODO RegEx is not working correctly.
    size = input('Please enter your size in m: ')
    if not re.match(r'\d\.', size):
        print('Use only numbers and one dot, like this example: "1.90"')
        return
    else:
        size = float(size)

    # Calculate the bmi.
    bmi = round(bmi_calculator(weight, size), 1)

    # Print the result in console.
    print('\nYour BMI is: {}'.format(str(bmi)))

    # Compare the actual bmi with the old one.
    bmi_compare(bmi)

    # Assign the actual date to history and create a list with the other data.
    his_date = '{:%B %d, %Y}'.format(datetime.datetime.now())
    history = [his_date, weight, size, bmi]

    # Write all data in a .csv file for the history.
    bmi_to_csv(history)

    # Job Done.
    print('Jobs done, goodbye')
    time.sleep(1)

# ===============================
#           MAIN PROGRAM
# ===============================


#   Main Program.
if __name__ == "__main__":
    #   Launch main menu.
    main()