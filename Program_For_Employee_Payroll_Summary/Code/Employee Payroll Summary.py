# Programmer: Tofig Gasimov
# Completion Date: 2/19/2022

# Objectives of program

"""
-Open text file, extract and manipulate data for various calculations by looping menu continuously
-Make use of functions to make it easy to read/understand main()/code
-Make use of lists
-and so on.
"""

# Purpose of program

"""
Program reads employee work data from a text file and then calculates payroll information based on this file.
Text file contains one line of text for each employee. Each line consists of the following data (delimited by tabs):

Columns:

1) employee's name
2) employee's hourly wage rate
3) hours worked Monday
4) hours worked Tuesday
5) hours worked Wednesday
6) hours worked Thursday
7) hours worked Friday

In total, Text file consists of 6 rows and 7 columns
"""

import sys


def inputUserChoiceF():
    # Purpose of this function is to loop menu continuously
    while True:

        print('''
Menu of choices:
                    (r)ead employee data
                    (p)rint employee payroll
                    (d)isplay an employee by name
                    find (h)ighest paid employee
                    find (l)owest paid employee
                    (q)uit
        ''')

        menu_choice = input('Please enter your choice: ')
        if menu_choice == "r" or menu_choice == "p" or menu_choice == "d" or menu_choice == "h" \
                or menu_choice == "l" or menu_choice == "q":
            break
        else:
            print('Invalid choice, please try again.')
            continue
    # Return entered menu choice
    return menu_choice


def readEmployeeDataF(x):
    try:
        text = open(x, 'r')  # Open file
        overall_lst = text.readlines()  # Read lines into variable overall_lst
        overall_lst.sort()  # Sort alphabetically

        for n in overall_lst:  # Read one line at a time

            # Split elements of overall_lst into further elements
            # ex:
            # overall_lst = ["Admad\t11.50\...","Smith\t10\t..."....]
            # line = ["Smith", "10",....]
            line = n.split()

            lstNames.append(line[0])  # Appending elements at index 0 (Name) to list lstNames
            lstWages.append(float(line[1]))  # Appending elements at index 1 (Wage per hour) to list lstWages

            # Calculate total hours worked and append to lstHoursWorked list
            total_hours = 0
            for i in range(2, 7):
                total_hours = total_hours + float(line[i])
            lstHoursWorked.append(total_hours)

            # Calculate total pay and append to lstTotalPay list
            # It is optional and required for the ease of findHighOrLowEmployeeF function
            total_pay = 0
            for i in range(0, len(lstNames)):
                total_pay = lstHoursWorked[i] * lstWages[i]
            lstTotalPay.append(total_pay)
        print("File has been read")
        text.close()  # Close file

    except IOError:  # Exception handling for non-existent file
        print("Error reading file", x)


def printPayrollF():  # Displaying Payroll table
    # If file has not been read yet
    if len(lstNames) == 0:
        print("Employee data has not been read.")
        print("Please read the file before making this choice.")
    else:
        total_payroll = 0
        print("\nName\t Hours\t Pay")
        print("-----\t -----\t -----")

        # Printing Payroll table

        for i in range(0, len(lstNames)):
            print(lstNames[i], "\t", lstHoursWorked[i], "\t", f"${lstTotalPay[i]:,.2f}")  # Printing Rows
        print("\nTotal Payroll =", f"${sum(lstTotalPay):,.2f}")  # Printing total payroll


def findEmployeeByNameF(lst, n, key):  # Linear Search
    # Parameters: list, length of list and key word to search for
    # Searching list sequentially
    for i in range(0, n):
        if lst[i] == key:  # If keyword is found within the list, return index of the keyword
            return i
    return -1  # If keyword is not found, return -1


def findHighOrLowEmployeeF(x):  # Finding the highest/lowest earned employee and amount (total pay per week)
    if x == "h":  # If user wants to know the highest earned employee
        highest = max(lstTotalPay)  # Finding maximum in total pay list
        # Calling and passing arguments to findEmployeeByNameF (Linear search function)
        # to identify the index of the highest total pay per week in total pay list
        search_highest = findEmployeeByNameF(lstTotalPay, len(lstTotalPay), highest)
        print(lstNames[search_highest], "is the highest paid and earned", f"${highest:,.2f}")
    elif x == "l":  # If user wants to know the lowest earned employee
        lowest = min(lstTotalPay)  # Finding minimum in total pay list
        # Calling and passing arguments to findEmployeeByNameF (Linear search function)
        # to identify the index of the lowest total pay per week in total pay list
        search_lowest = findEmployeeByNameF(lstTotalPay, len(lstTotalPay), lowest)
        print(lstNames[search_lowest], "is the lowest paid and earned", f"${lowest:,.2f}")


# Creating global lists
lstNames = []
lstWages = []
lstHoursWorked = []
lstTotalPay = []  # Optional


def main():
    while True:

        menu_choice = inputUserChoiceF()

        if menu_choice == "r":
            file_name = input('Enter the file name: ')
            readEmployeeDataF(file_name)  # Calling readEmployeeDataF function

        elif menu_choice == "p":
            printPayrollF()  # Calling printPayrollF function

        elif menu_choice == "d":
            # If file has not been read yet
            if len(lstNames) == 0:
                print("Employee data has not been read.")
                print("Please read the file before making this choice.")
            else:
                name = input("Enter the employee's name: ")  # Prompt to enter name for search
                # Handling entered names that are not capitalized
                # and calling findEmployeeByNameF function to do linear search
                search_name = findEmployeeByNameF(lstNames, len(lstNames), name.capitalize())
                if search_name == -1:  # If name is not found
                    print(name.capitalize(), "is not found in the list.")
                else:  # If name is found within lstNames
                    total_pay = (lstHoursWorked[search_name] * lstWages[search_name])  # Calculate pay
                    wage_per_hour = total_pay / lstHoursWorked[search_name]  # Calculate wage per hour
                    print(name.capitalize(), "worked", lstHoursWorked[search_name], "hours at",
                          f"${wage_per_hour:,.2f}", "per hour, and earned", f"${total_pay:,.2f}")

        elif menu_choice == "h":
            # If file has not been read yet
            if len(lstNames) == 0:
                print("Employee data has not been read.")
                print("Please read the file before making this choice.")
            else:
                findHighOrLowEmployeeF("h")  # Calling findHighOrLowEmployeeF function and passing h as argument

        elif menu_choice == "l":
            # If file has not been read yet
            if len(lstNames) == 0:
                print("Employee data has not been read.")
                print("Please read the file before making this choice.")
            else:
                findHighOrLowEmployeeF("l")  # Calling findHighOrLowEmployeeF function and passing h as argument

        elif menu_choice == "q":
            print("\nGoodbye!")
            sys.exit()  # Terminate program


main()
