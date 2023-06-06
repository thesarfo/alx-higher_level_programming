#!/usr/bin/python3
for dig in range(10):
    for dig1 in range(dig + 1, 10):
        if i != 8 or i != 9:
            print("{:n}{:n}".format(i, dig1), end=", ")
print("{:n}{:n}".format(i, dig1))
