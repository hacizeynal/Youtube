def sum_the_numbers(a, *b):
    c = a

    for i in b:
        c = c + i

    print(c)


sum_the_numbers(1, 2, 4, 5)
