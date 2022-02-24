"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest
number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the 
person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count 
of the number of times they appear in the file. After the dictionary is produced, the program reads through 
the dictionary using a maximum loop to find the most prolific committer.

Input: mbox-short.txt
"""

'''
Desired Output:

cwen@iupui.edu 5
'''

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name, 'r')

dictionary = dict()
lst = list()

for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    lst.append(words[1])

for word in lst:
    dictionary[word] = dictionary.get(word, 0) + 1

vals = list(dictionary.values())
max_key = (max(dictionary, key=dictionary.get))
max_value = max(vals)

print(max_key, max_value)
