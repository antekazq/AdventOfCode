import os

#Reading data
def read_from_file(filename):
    """
    Reads integers from a file and returns them as a list.
    
    Args:
        filename (str): The path to the file containing data.
        
    Returns:
        list[int]: A list of integers read from the file.
    """

    with open (filename, 'r') as file:

        split_data = file.read().split()
        num_data = [int(i) for i in split_data]

    return num_data


#Read data from file
file_path = os.path.join(os.path.dirname(__file__),'Day1_input.txt')
num_data = read_from_file(file_path)

#Split data into two separate lists
left = (num_data[0:len(num_data):2])
right = (num_data[1:len(num_data):2])

#Initialize total sum and counter
total = 0 #Holds the final result
counter = 0 #Tracks the count of matches between elements in left and right

#Compare elements
for i in left:   
    for j in right:
        if i == j: #Check for matches between elements
            counter += 1

    #Add the product of the element and its match count to the total
    total = total + i*counter

    #Reset the counter for the next element
    counter = 0

print("Total:", total)