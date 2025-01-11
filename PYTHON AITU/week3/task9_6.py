set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common_items = set1 & set2
if common_items:
    print("Two sets have items in common", common_items)
else:
    print("No common items")
