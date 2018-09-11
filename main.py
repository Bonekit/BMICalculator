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
import BMI

# ===============================
#       MAIN FUNCTIONS
# ===============================

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

    # Initialize BMI_Handler Class.
    bmi = BMI.BMI_Handler(weight, size)

    # Print the result in console.
    print('\nYour BMI is: {}'.format(str(bmi.bmi_calculator())))

    # Assign the actual date to history and create a list with the other data.
    his_date = '{:%B %d, %Y}'.format(datetime.datetime.now())
    history = [his_date, weight, size, bmi]

    # Compare the actual bmi with the old one.
    bmi.bmi_compare(history)

    # Write all data in a .csv file for the history.
    bmi.bmi_to_csv(history)

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