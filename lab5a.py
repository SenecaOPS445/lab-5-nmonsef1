#!/usr/bin/env python3
# Author ID: nmonsef

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r') # Open the file in read mode
    contents = f.read() # Read the entire file
    f.close()  # Close the file
    return contents # Return the contents 


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r') # Open the file in read mode
    read_data = f.read() # Read the entire contents 
    f.close() # Close the file
    read_data.split('\n')  # Split the contents by newline characters 
    list_lines = read_data.split('\n') # Store the lines into list_lines
    non_empty_lines = [] # Initialize an empty list to hold non-empty lines
    for line in list_lines:
        if line != '': # Check if the line is not empty
            non_empty_lines.append(line) 
    return non_empty_lines


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
