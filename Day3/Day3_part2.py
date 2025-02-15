
import os
import re

def read_from_file(filename):
    """
    Reads a file and returns a string.

    Args:
        filename (str): Path to input file.

        Returns:
            String: A string of all the characters. 
    """
    with open (filename, 'r') as file:
        return file.read()

#Read content from input file
file_path = os.path.join(os.path.dirname(__file__),'Day3_input.txt')
input_string = read_from_file(file_path)

#Extract relevant parts from the input string using regular expressions
#This includes 'mul(X,Y)' operations and 'do()'/'don't()' commands
coefficients = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", input_string)


#Flag to control whether 'mul' operations should be added based on 'do()' and 'don't()' commands
enabled = True

#List to store 'mul' operations that are considered "enabled"
all_do = []

#Iterate over each operation/command extracted from the input
for c in coefficients:
    if c == "do()":
        enabled = True
        continue
    if c == "don't()":
        enabled = False
        continue
    if enabled:
        all_do.append(c)

print(all_do)


#Extract numerical values from the 'mul' operations
coefficients = re.findall("mul\((\d{1,3}),(\d{1,3})\)", str(all_do))

#Calculate the sum of products of the 'mul' operations
int_coefficients = sum([(int(x) * int(y)) for x, y in coefficients])

#Output the final sum
print('Final sum of mul(X,Y) multiplications:', int_coefficients)


