elements = [3, 1, 2, 2, 3, 4, 4, 4, 5, 5, 8, 8]
duplicates = []
for x in elements:
    if elements.count(x) > 1 and x not in duplicates:
        duplicates.append(x)
print(duplicates)
