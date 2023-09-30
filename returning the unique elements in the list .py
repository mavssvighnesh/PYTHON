def unique(lst):
    unique_elements = []

    for item in lst:
        if item not in unique_elements:
            unique_elements.append(item)

    return unique_elements
my_list = [1, 2, 3, 4, 3, 2, 5, 6, 4]
result = unique(my_list)
print("The unique elements in the list is:")
print(result)  # Output: [1, 2, 3, 4, 5, 6]