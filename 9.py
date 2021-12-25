

def revnum(num):

    if num[::-1] == num:
        print("True")

    else:
        print("False")

num = input("Enter number: ")

revnum(num)