# Title                 : BMI-Calculator
# Description           : BMI-Calculator as Test Project
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
    return weight / size **2


def bmi_to_csv(history):
    csv_dialect = csv.register_dialect('csv_dialect', delimiter=',', quotechar='"')
    with open('./output/history.csv', 'a', encoding='UTF-8') as file:
        writer = csv.writer(file, dialect=csv_dialect)
        writer.writerow(history)

# Main Function to calculate the bmi.


def main():
    # Welcome.
    subprocess.call('cls', shell=True)
    print('Welcome to the BMI-Calculator v1.0')

    # User Input to get weight and size.
    weight = input('Please enter your weight in kg: ')
    if not re.match(r'\d', weight):
        print('Enter only numbers please')
        return
    else:
        weight = float(weight)

    # TODO RegEx is not working correctly.
    # TODO Round values.
    size = input('Please enter your size in m: ')
    if not re.match(r'\d', size):
        print('Enter only numbers please')
        return
    else:
        size = float(size)

    # Calculate the bmi.
    bmi = round(bmi_calculator(weight, size), 1)

    # Print the result in console.
    print('\nYour BMI is: {}'.format(str(bmi)))

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