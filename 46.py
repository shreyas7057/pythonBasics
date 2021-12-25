str1 = "America"
str2 = "Japan"

firs_char_str1 = str1[0]
print(firs_char_str1)
middle_char_str1 = int(len(str1)/2)
middle_char_str1 = str1[middle_char_str1]
print(middle_char_str1)

first_char_str2 = str2[0]
print(first_char_str2)

rem_st2 = str2[2:]
print(rem_st2)

newstring = firs_char_str1+""+first_char_str2+""+middle_char_str1+""+rem_st2
print(newstring)