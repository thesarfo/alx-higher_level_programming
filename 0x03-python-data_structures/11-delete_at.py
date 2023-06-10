#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''deletes item at a specific list position'''
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
    return my_list
