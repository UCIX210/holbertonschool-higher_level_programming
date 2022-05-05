def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    list2 = my_list
    for i in range(len(list2)):
        if list2[i] == search:
            list2[i] = replace
    return (list2)
