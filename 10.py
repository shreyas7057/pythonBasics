l1 = [10, 20, 23, 11, 17]
l2 = [13, 43, 24, 36, 12]
l3 = []

def filterevenodd():

    for num in l1:
        if num%2!=0:
            print(num)
            l3.append(num)

    for num1 in l2:
        if num1%2==0:
            print(num1)
            l3.append(num1)
    print(l3)
filterevenodd()