input_list = input("Please enter number of  list separated by comma : ")
converted_to_list = input_list.split(",")
converted_to_list = list(map(int,converted_to_list))
# print(converted_to_list)


def count_even_odd(converted_to_list):
    even = 0
    odd = 0

    for i in converted_to_list:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1

    return even, odd


even, odd = count_even_odd(converted_to_list)

print("Number of even numbers = {} and Number of Odd numbers = {}".format(even, odd))
