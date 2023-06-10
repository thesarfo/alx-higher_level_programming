#!/usr/bin/python3
def multiple_returns(sentence):
    '''returns a tuple with the length of a string and its first character'''
    if sentence == "":
        length = 0
        first_char = None
    else: 
        length = len(sentence)
        first_char = sentence[0]
    tuple_res = (length, first_char)
    return tuple_res
