a = int(input("Enter number: "))
b = int(input("Enter number: "))

res = a*b

if res > 1000:
    res = a+b
    print("Addition is {0}".format(res))

else:
    print(res)