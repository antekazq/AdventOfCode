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


distance = 0

#Loop until list is empty
#And calculate the absolute difference between the smallest values
while len(left) > 0:
    distance = distance + abs(min(left) - min(right))
    left.remove(min(left))
    right.remove(min(right))

print ("Answer:", distance)


#-----------------------------
#Part 2

# total = 0
# counter = 0

# for i in left:   
#     for j in right:
#         if i == j:
#             counter += 1
#             print(i, j, counter)
             

#     print(counter)
#     total = total + i*counter
#     counter = 0

# print(total)

    

    



    

