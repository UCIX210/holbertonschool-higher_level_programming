#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list2 = my_list.copy()
    list2[search] = replace
    return list2
