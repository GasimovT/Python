# Programmer: Tofig Gasimov
# Completion Date: 2/24/2022

# Purpose of program:

'''
This is a small-sized number translator that translates integer
numbers by taking input from the user into Spanish word form.
'''


def main():
    # Opening and reading file into dictionary
    dictionary = dict()
    file_d = open('words.txt', 'r', encoding='utf-8')  # Ensuring letter é passes successfully
    for line in file_d:
        words = line.split()
        dictionary[int(words[0])] = words[1]
    print(dictionary)

    while True:
        try:
            # Prompt user to enter number
            number = int(input("Please enter number between 1 and 100 (type 0 to quit): "))
            # If number is within range of 1 and 100, print result and continue to loop
            if 0 < number <= 100:
                print("\nThe Spanish translation of", number, "is", dictionary[number], "\n")
                continue
            # To break out of loop
            elif number == 0:
                break
        except:
            print("\nPlease enter valid number between 1 and 100 (type 0 to quit).\n")


main()
