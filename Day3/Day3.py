import re
import os

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
    
#Read ths file and store in input_string
file_path = os.path.join(os.path.dirname(__file__),'Day3_input.txt')
input_string = read_from_file(file_path)


#Use regular expressions to find all occurrences of the 'mul(X, Y)' pattern in the input string
#This regex extracts pairs of numbers used in the multiplication
coefficients = re.findall("mul\((\d{1,3}),(\d{1,3})\)", input_string)

#Calculate the sum of the products of these number pairs
#The list comprehension iterates through all pairs, converting them to integers and multiplying them
int_coefficients = sum([(int(x) * int(y)) for x, y in coefficients])

#Output the final computed sum of all multiplications to the console
print('Final sum of mul(X,Y) multiplications:', int_coefficients)
