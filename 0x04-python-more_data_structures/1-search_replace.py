#!/usr/bin/python3
def replace_search(my_list, search, replace):
    def search_find(element):
        return element if element != search else replace
    return list(map(find_search, my_list))
