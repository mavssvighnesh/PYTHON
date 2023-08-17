
def dups(lst):
    duplicates = []
    seen = set()

    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates
my_list = [1, 2, 3, 4, 3, 2, 5, 6, 4]
result = dups(my_list)
print("The duplictes of the list is:")
print(result)  # Output: [3, 2, 4]