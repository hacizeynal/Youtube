from array import *

new_array = array("i", [ ])

length_of_array = int(input("Please enter length of Array: \n"))

for i in range(length_of_array):
    value_of_array = int(input("Please enter value for array: "))
    new_array.append(value_of_array)

print(new_array)

value_for_search = int(input("Please enter value to search in Array: \n"))

index = 0
for j in new_array:
    if j == value_for_search:
        print(index)
        break

    index = index + 1

# print(new_array.index(value_for_search))
