list1 = ["hello ", "take "]
list2 = ["dear", "sir"]

result = [a + b for a in list1 for b in list2]

print(result)