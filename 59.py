sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = dict()
for i in sampleList:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1

print(count)