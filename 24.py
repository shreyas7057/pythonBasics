with open('test.txt','r') as fp:
    rr = fp.readlines()
    print(rr[5])

fp.close()