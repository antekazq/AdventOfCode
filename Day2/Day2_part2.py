import os 

def read_from_file(filename):
    """
    Reads a file and returns a list of lists of integers.

    Args:
        filename (str): Path to input file.

        Returns:
            list: A list where each item is a list of integers from each line in the file.
    """
    with open (filename, 'r') as file:
        rows = [] 

        for line in file:
            #Ignore empty lines
            if line.strip():
                numbers = line.split()
                #Convert to int
                numbers = [int(num) for num in numbers]
                rows.append(numbers)
    return rows


#Get file path for input data
file_path = os.path.join(os.path.dirname(__file__),'Day2_input.txt')

#Load data from input file
data = read_from_file(file_path)
    

#Requirements to pass:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

#Initializing counter for safe lists and storage list for non-safe lists
safe_counter_part1 = 0 
rejected_data = []

for lst in data: 
    if ((lst == sorted(lst) or lst == sorted(lst, reverse=True)) and
        len(lst) == len(set(lst)) and
        all(abs(lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1))):
        #Increase safe count if requirements are met
        safe_counter_part1 += 1 
    else:
        #Collect rejected data to pass through "Problem Dampener"
        rejected_data.append(lst)


def problem_dampener(lst):
    """
    Checks if a list becomes valid after removing one element.

    Args:
        lst (list): A list of integers to check.
    
    Returns:
        bool: True if the modified list meets the safety criteria, False otherwise.
    """

    if ((lst == sorted(lst) or lst == sorted(lst, reverse=True)) and
            len(lst) == len(set(lst)) and
            all(abs(lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1))):
        return True
    else:
        return False


#Process rejected lists with "Problem Dampener"
safe_counter_part2 = 0

for rejects in rejected_data:
    for i in range(len(rejects)):
        #Remove one element and check if the list becomes valid
        if problem_dampener(rejects[:i]+rejects[i+1:]):
            #Increase safe count if list is fixed
            safe_counter_part2 +=1
            break

print('number of safe from part1 and 2:', safe_counter_part2 + safe_counter_part1)

