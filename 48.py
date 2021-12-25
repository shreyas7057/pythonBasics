str1 = "P@#yn26at^&i5ve"

sm_count=cap_count=di_count=sym_count = 0


for i in str1:

    if i.islower():
        sm_count+=1

    elif i.isupper():
        cap_count+=1
    
    elif i.isnumeric():
        di_count+=1
    
    else:
        sym_count+=1

print("Small Char count = {0}, Captial Count = {1}, Digit Count = {2}, Symbol Count {3}".format(sm_count,cap_count,di_count,sym_count))
        
    