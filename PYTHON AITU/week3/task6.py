list1 = ["I", "am", "learning"]
list2 = ["Python", "programming", "!"]

result = [i + " " + j for i, j in zip(list1, list2)]
print(result)
