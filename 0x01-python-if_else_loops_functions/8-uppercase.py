#!/usr/bin/python3
def uppercase(str):
	for char in str:
	    ascii_v = ord(str)
	    if 97 <= ascii_v <= 122:
	        char_upp = chr(ascii_v - 32)
	    else:
		char_upp = char
	    print(char_upp, end="")
	print()
