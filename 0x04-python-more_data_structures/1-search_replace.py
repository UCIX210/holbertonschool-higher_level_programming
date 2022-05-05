def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    list2 = my_list
    for i in range(len(list2)):
        if list2[i] == search:
            list2[i] = replace
    return (list2)
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
