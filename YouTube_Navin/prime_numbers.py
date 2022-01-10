while True:
    num = int(input("Please enter a number to check if it is Prime number or not: "))

    for i in range(2,num):
        if num % i == 0:
            print("This is a not prime number ,try again please !")
            break
    else:
        print("Congratulations ,this is Prime number :) ! ")
