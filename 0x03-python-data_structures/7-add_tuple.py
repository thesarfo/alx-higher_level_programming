#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''adds two tuples'''
    elems_a = tuple_a[:2] + (0, 0)
    elems_b = tuple_b[:2] + (0, 0)
    result = (elems_a[0] + elems_b[0], elems_a[1] + elems_b[1])
    return result
