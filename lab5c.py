#!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        return int(number1) + int(number2) # Try to convert inputs to integers and add them
    except ValueError: # Handle the case where conversion to integer fails
        return 'error: could not add numbers'


def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r') # Try to open the file in read mode 
        list_of_lines = f.readlines()
        f.close()
        return list_of_lines # Return the list of lines
    except FileNotFoundError: # Handle the case where the file is not found
        return "error: could not read file"

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception