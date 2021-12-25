list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
newli = []
for i in list1:
    if i%5==0 and i<=150:
        newli.append(i)
print(newli)