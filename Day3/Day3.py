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

file_path = os.path.join(os.path.dirname(__file__),'Day3_input.txt')
input_string = read_from_file(file_path)

coefficients = re.findall("mul\((\d{1,3}),(\d{1,3})\)", input_string)

int_coefficients = sum([(int(x) * int(y)) for x, y in coefficients])

print('Final sum of mul(X,Y) multiplications:', int_coefficients)
