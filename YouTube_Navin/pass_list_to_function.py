def count_even_odd(test_with_manual_list):
    even = 0
    odd = 0

    for i in test_with_manual_list:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    return even, odd


# input_list = input("Please enter number of  list separated by comma : ")
# converted_to_list = input_list.split(",")

test_with_manual_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
even, odd = count_even_odd(test_with_manual_list)

print("Number of even numbers are : ", even)
print("Number of odd numbers are : ", odd)
