def outer(a,b):

    def inner():
        add = a+b
        return add

    res = inner()

    mainres = res+5
    print(mainres)


outer(1,2)