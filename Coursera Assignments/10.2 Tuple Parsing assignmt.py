'''

10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of
the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second
time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

Input: mbox-short.txt
'''

'''
Desired output:

04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
'''

name = input("Enter file:")
lst=list()
lst1=list()
lst2 = list()
dictionary=dict()
handle = open(name, 'r')

# Splitting each word in line
for line in handle:
    if not line.startswith('From '):
        continue
    words=line.split()
    lst.append(words[5]) # Appending index 5 (whole time set) to list

# Splitting time with semicolon
for line in lst:
    hours=line.split(':')
    lst1.append(hours[0]) # Appending hour to list1

# Adding items from list to dictionary and counting each of item's occurrence
for line in lst1:
    dictionary[line]=dictionary.get(line, 0)+1

# Sort the dictionary by value using items()
# The items() method returns a view object
# The view object contains the key-value pairs of the dictionary, as tuples in a list

for key, val in dictionary.items():
    lst2.append((key, val))

lst2.sort()

# Printing desired output
for key, val in lst2:
    print(key, val)

