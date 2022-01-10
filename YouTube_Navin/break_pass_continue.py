# The break statement terminates the loop containing it. Control of the program flows to the statement
# immediately after the body of the loop.
# If the break statement is inside a nested loop (loop inside another loop),
# the break statement will terminate the innermost loop.


def test_break():
    y = int(input("How many apple do you want ?: "))

    i = 1
    available_in_market = 5

    # break is used for jumping out of loop in case we match the condition

    while i <= y:
        if i > available_in_market:
            print("We are out of stock unfortunately ")
            break
        print("Apple")
        i = i + 1

    print("Enjoy your apples :) ")


# print(test_break())


# The continue statement is used to skip the rest of the code inside a loop for the current iteration only.
# Loop does not terminate but continues on with the next iteration.

def test_continue():
    for k in range(1, 101):
        if k % 3 == 0 or k % 5 == 0:
            continue
        print(k)


# print(test_continue())

# pass is used for ignoring piece of code ,like comment ,but in this case interpeter is checking this code
# ignoring this code ,it works like placeholder.


def test_pass():
    for z in range(2, 200):
        if z % 2 != 0:
            pass
        else:
            print(z)


print(test_pass())
