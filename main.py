# Title                 : BMI-Calculator
# Description           : BMI-Calculator as Test Project
# Author                : Tobias Menzel
# Date                  : 10.09.2018
# Notes                 :
# Python_version        : 3.6.6
# ==========================================================================================

# ===============================
#       MAIN FUNCTIONS
# ===============================

# Calculator to calculate the bmi.
def bmi_calculator(weight, size):
    yield ((weight / size)^2)

# Main Function to calculate the bmi.
def main():
    print('Welcome to the BMI-Calculator v1.0')
    weight = input('Please enter your weight in kg:')
    size = input('Please enter your size in cm:')
    print('Your BMI is: {}'.format(bmi_calculator(weight, size))


if __name__ == '__main__':
    main()