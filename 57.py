l1 = [34, 54, 67, 89, 11, 43, 94]

print("Removing index 4 value")
four_index = l1.pop(4)
print(f"Removing the index {l1}.")

l1.insert(2,four_index)
print(f"Inserting at 4th index {l1}.")

l1.append(four_index)
print(f"Appending the number {l1}.")