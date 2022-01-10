input_list_names = input("Please enter names of  list separated by comma : ")
converted_to_list_names = input_list_names.split(",")

list_length_bigger_than_five = [ ]


def checking_names_length(list_arg):
    for each_item in list_arg:
        if len(each_item) > 5:
            list_length_bigger_than_five.append(each_item)
    if len(list_length_bigger_than_five) == 0:
        print("Please enter again ,you should enter at least one name with length 5")
    else:
        print(list_length_bigger_than_five)


checking_names_length(converted_to_list_names)

