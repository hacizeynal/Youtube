my_list = [1,5,10,15,20,25,30,33,38,39]

for k in my_list:

    if k % 7 ==  0:
        print(k)
        break
else:
    print("Not found")