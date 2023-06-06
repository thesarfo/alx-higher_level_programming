#!/usr/bin/python3
for dig in range(10):
    for dig1 in range(dig + 1, 10):
        if dig != 8 or dig1 != 9:
            print("{:n}{:n}".format(dig, dig1), end=", ")
print("{:n}{:n}".format(dig, dig1))
