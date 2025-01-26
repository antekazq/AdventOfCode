import os #Used to handle file paths

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


#Filter lists that are sorted (ascending or descending) and have no duplicates
filtered_data = [lst for lst in data 
    if ((lst == sorted(lst) or lst == sorted(lst, reverse=True)) and len(lst) == len(set(lst)))]

#Keep on filtering lists where all adjacent numbers differ by at most 3
final_data = [lst for lst in filtered_data 
              if all(abs(lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1))]

#Display the number of valid lists ("reports") that passed all checks
print("Number of safe reports:", len(final_data))






