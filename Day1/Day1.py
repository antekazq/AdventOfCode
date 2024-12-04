import os

#Reading data

right = []
left = []

f = open("Day1_input.txt", "r")
data = f.read()

split_data = data.split()
num_data = []

for i in split_data:
    num_data.append(int(i))

left = (num_data[0:len(num_data):2])
right = (num_data[1:len(num_data):2])

#---------------------------
#Part 1

"""
distance = 0

while len(left) > 0:
    distance = distance + abs(min(left) - min(right))
    left.remove(min(left))
    right.remove(min(right))

print ("Answer:", distance)
"""

#-----------------------------
#Part 2

total = 0
counter = 0

for i in left:   
    for j in right:
        if i == j:
            counter += 1
            print(i, j, counter)
             

    print(counter)
    total = total + i*counter
    counter = 0

print(total)

    

    



    

