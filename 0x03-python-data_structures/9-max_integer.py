#!/usr/bin/python3
def max_integer(my_list=[]):
    '''finds the biggest integer of a list'''
    if len(my_list) == 0:
        return None
    else:
        max_val = my_list[0]
        for element in my_list:
            if element > max_val:
                max_val = element
    return max_val
