# Programmer: Tofig Gasimov
# Completion Date: 2/10/2022

# Objectives of program

"""
-Define and use functions that accept and/or return values
-Apply data validation and try-except/Loop structures to prevent bad data from
entering a program
"""

# Purpose of program

"""
The program is designed for calculating personal finances based on a series of user inputs. 
The program should validate user's entries to prevent bad data from entering or crashing the program.
"""

# Some Instructions may not match word documents. Some of them has been updated by me
# to better serve the user and make their operations easier.
# Please see Pseudocode word document for more information

import sys
from datetime import date


# Defining Function
def is_NumFloat(x):
    # Checking for a float string (using replace() + isdigit() methods) or all numeric string
    # Does not check for exponent values
    # Reason why we check for a float string is because of possible decimal point as input
    if x.replace('.', '', 1).isdigit() or x.isnumeric():
        num = x  # converting str into float
        return num
    else:
        # Otherwise display error message
        print("\nResponse must be numeric.\n")


# Defining function
def is_ValidName(x):
    # To require that string can contain at least one alpha and space, and only alphas and spaces
    if (any(y.isalpha() for y in x)  # at least one alpha
            and any(y.isspace() for y in x)  # at least one space
            and all(y.isalpha() or y.isspace() for y in x)):  # only alphas/spaces
        num = x
        return num
    else:
        # Otherwise, display error message
        print("\nResponse can only contain letters and space.\n")


# Defining function
def check_Date(x):
    y = x.split("/")  # Splitting string into a list. Specifies the separator as slash sign
    for n in y:  # looping through dt list
        if not n.isdigit():  # if not digit
            return "invalid_date"  # return invalid_date

    month = int(y[0])
    day = int(y[1])
    year = int(y[2])
    # checking to see whether entered DOB numbers fall into range
    # it does not check if the February 30 is invalid

    # it checks to see:
    # if month is withing range of 1 to 12
    if month < 1 or month > 12:
        return 'invalid_month'
    # if day is withing range of 1 to 31
    elif day < 1 or day > 31:
        return 'invalid_day'
    # if year is withing range of 1900 to Current
    elif year < 1900:
        return 'invalid_year'
    return 'True'


def main():
    # Global values
    global valid_name, net_salary, income_per_hour, valid_salary, dob

    # Loop until desired input it achieved
    while True:
        name = input("What is your first and last name?: ")  # Prompt user to enter first and last name
        if name == is_ValidName(name):  # calling function to check if input is valid
            valid_name = name  # assigning input to new variable
            break
        else:
            # Otherwise, error will be displayed from function and
            # loop will continue until desired input is achieved
            continue

    while True:
        # Prompt to enter float number and replace , or # sign
        salary = input("what is your annual salary?: ").replace("$", "").replace(",", "")
        if salary == is_NumFloat(salary):  # calling function to check if input is valid
            valid_salary = float(salary)  # assigning input to new variable and defining it as float
            break
        else:
            continue
    # If entered value for salary is less than 1000
    if valid_salary < 1000:
        # Creating infinite loop to achieve desired input
        while True:
            # Creating 2 lists
            yes_answer = ["Yes", "Y", "yes", "y", "YES"]
            no_answer = ["No", "NO", "N", "no", "n", ""]
            # Prompt user to enter yes or no
            salary_question = input("Did you enter annual salary (yes or no) ?: ")
            # If input is in yes_answer list then break
            if salary_question in yes_answer:
                break
            # If input is in no_answer list then display error message and exit program
            elif salary_question in no_answer:
                print("\nAnnual salary should be at least $1,000")
                print("Please restart program again.\n")
                sys.exit()
            # Else, display error message and prompt user to enter
            # value again and loop until desired input is achieved
            else:
                print("\nPlease try to answer {yes, y} as yes or {no, n} as no.\n")
                continue

    while True:
        try:
            dob = input("Enter your date of birth in the format MM/DD/YYYY: ")
            dob_status = check_Date(dob)  # calling function to see if entered input is valid
            if dob_status == 'True':  # if input is valid then break out of loop
                break
            # if format is not valid, display error message and loop until desired input is achieved
            if dob_status == 'invalid_date':
                print("\nEnter date in proper format of MM/DD/YYYY only.\n")
                continue
            # if month range is not valid, display error message and loop until desired input is achieved
            elif dob_status == 'invalid_month':
                print("\nMonth must be between 1 and 12.\n")
                continue
            # if day range is not valid, display error message and loop until desired input is achieved
            elif dob_status == 'invalid_day':
                print("\nDay must be between 1 and 31.\n")
                continue
            # if year is not valid, display error message and loop until desired input is achieved
            elif dob_status == 'invalid_year':
                print("\nYear can only be after 1900.\n")
                continue
        except:
            # Additional exception handling in case if entered format is 11/112011 or anything else
            print("\nSomething went wrong, please try again.\n")
            continue

    while True:
        try:
            hours_per_week = float(input("How many hours do you work per week on average? : "))
            # If entered value is float
            if hours_per_week:
                # Calculate income per week and hour
                income_per_week = valid_salary / 52
                income_per_hour = income_per_week / hours_per_week
                print(f"\nYour hourly wage is approximately ${income_per_hour:,.2f} per hour\n")
                break
        except:
            # Else, print error message and loop until desired input is achieved
            print('\nResponse must be numeric.\n')
            continue

    while True:
        try:
            tax_rate = float(input('What is your effective tax rate? (0.27 is common): '))
            # If entered value is float and within range of 0 and 1
            if 0.0 < tax_rate < 1.0:
                tax = tax_rate * valid_salary
                net_salary = valid_salary - tax
                print(f"\nYou pay an estimated ${tax:,.2f} to taxes per year.")
                print(f"You effectively earn ${income_per_hour - income_per_hour * tax_rate:,.2f} per hour after "
                      f"taxes.\n")
                break
            else:
                # if entered value is float but not within range of 0 and 1
                print('\nPlease enter decimal between 0 and 1.\n')
                continue
        except:
            # if entered value is not float, display error message and loop until desired input is achieved
            print('\nPlease enter percentage % as decimal.\n')
            continue

    while True:
        # Prompt to enter float number and replace , or # sign
        expenses = input(f'{valid_name.split()[0].title()}, list your expenses per month: ').replace("$", "").replace(
            ",", "")
        if expenses == is_NumFloat(expenses):  # calling function to validate input
            # if input is valid, assign expense variable to another variable and define it as float
            valid_expense = float(expenses)
            # calculate saving amount
            saving = net_salary - valid_expense * 12
            # if user breaks even
            if saving == 0:
                print("\nYou are breaking even.\n")
                break
            # if user spent too much
            elif saving < 0:
                print(f"\nYou are going into debt by ${abs(saving / 12):,.2f} each month.\n")
                break
            # if user have extra money to save
            elif saving > 0:
                print(f'\nYou have ${saving / 12:,.2f} available for saving each month.\n')
                break
        else:
            continue

    while True:
        yes_answer = ["Yes", "Y", "yes", "y", "YES"]
        no_answer = ["No", "NO", "N", "no", "n", ""]
        # Prompt user to see if printout of answers is needed
        printout_question = input("Would you like a printout of your responses? ")
        # if answer to question is yes, then display name (capitalized first and last), DOB + calculate age,
        # and Net annual salary amount
        if printout_question in yes_answer:
            print("Name:", valid_name.title())
            age = date.today().year - int(dob.split('/')[2])
            print(f"Date of Birth: {dob} ({age} years old this year)")
            print(f'Net annual salary: ${net_salary:,.2f}')
            break
        # if answer to question is no, program terminates
        elif printout_question in no_answer:
            print("\nProgram has been terminated successfully.")
            sys.exit()
        # if answer is else, display error message and loop until desired input is achieved
        else:
            print("\nPlease try to answer {yes, y} as yes or {no, n} as no.\n")
            continue


main()
