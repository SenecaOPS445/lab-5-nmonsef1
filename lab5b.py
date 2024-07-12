#!/usr/bin/env python3
# Author ID: nmonsef

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r') # Open the file in read mode
    content = f.read() # Read the entire file
    f.close()  # Close the file
    return content # Return the contents 


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
def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')# Open the file in append mode
    f.write(string_of_lines)# Write the string to the file
    f.close()# Close the file

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')# Open the file in write mode
    for items in list_of_lines:
        f.write(items + '\n')# Write each item to the file followed by a newline
    f.close()
    
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    file_read = open(file_name_read, 'r')
    data = file_read.readlines()# Read all lines from the file
    file_read.close()

    file_write = open(file_name_write, "w")
    counter = 1 #nitialize a counter for line numbers
    for line in data:
        # Add line number to the beginning of each line
        line_with_number = str(counter) + ':' + line
        # Write the modified line to the new file
        file_write.write(line_with_number)
        counter += 1
    file_write.close()


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))