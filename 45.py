def appendMiddle(s1, s2):
  middleIndex = int(len(s1) /2)
  print("Original Strings are", s1, s2)
  middleThree = s1[:middleIndex:]+ s2 +s1[middleIndex:]
  print("After appending new string in middle", middleThree)
  
appendMiddle("Ault", "Kelly")