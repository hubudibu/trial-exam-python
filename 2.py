# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file does not exist, just return 0.
import os.path

def count_as(filename):
    counter = 0
    if os.path.exists(filename):
        for i in filename:
            if i == 'a':
                counter += 1
    return counter

print(count_as('korte.txt'))
