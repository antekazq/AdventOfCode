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


#Filter lists that are sorted (ascending or descending) and have no duplicates
filtered_data = []
rejected_data = []

for lst in data:
    if ((lst == sorted(lst) or lst == sorted(lst, reverse=True)) and len(lst) == len(set(lst))):
        filtered_data.append(lst)  
    else:
        rejected_data.append(lst)   

#Keep on filtering lists where all adjacent numbers differ by at most 3
final_data = []      
 

for lst in filtered_data:
    #Check if all adjacent numbers differ by 3 or less
    if all(abs(lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1)):
        final_data.append(lst)      
    else:
        rejected_data.append(lst)

print("antal rejected först: ", len(rejected_data))
#print("Antal remaining:", len(remaining_rejected_data))


#For part 2
def problem_dampener(rejected):
    """
    Handles lists rejected from earlier filtering by attempting to fix them
    with the Problem Dampener logic (removing one "bad" level).
    """
    safe_with_dampener = []

    #Iterate through each rejected list
    for lst in rejected:
        seen = set()
        duplicates = set()

        deleted = False

        #Identify duplicates
        for num in lst:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)

        #Remove one instance of the duplicate
        #Iterate backward for safe removal
        for i in range(len(lst) - 1, -1, -1):  
            if lst[i] in duplicates:
                del lst[i]
                deleted = True
                break  #Remove only one instance

        if deleted == True:
            break
        
        #Work in progress (!)
        #Check ascending/descending and if step is 3+/-



        #Check if the cleaned list is already safe
        if ((lst == sorted(lst) or lst == sorted(lst, reverse=True)) and
            len(lst) == len(set(lst)) and
            all(abs(lst[i + 1] - lst[i]) <= 3 for i in range(len(lst) - 1))):
            safe_with_dampener.append(lst)  #Directly append the list
            continue  

        

    return safe_with_dampener

#Currently debugging(!)
print("final data from part 1: ", len(final_data))
safe = problem_dampener(rejected_data)
print("safe after method: ", len(safe))
print("total safe after problem dampener: ", len(final_data) + len(safe))       

#Testing at the moment            
rejectedd = [ 
    [1, 2, 7, 8, 9],  
    [9, 7, 6, 2, 1],  
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],  
    [8, 6, 4, 4, 4, 1]
]

print(problem_dampener(rejectedd))







