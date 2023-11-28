#!/usr/bin/python3
string = ""

for i in range(97, 123):
    if i != 113 or i != 101:
        string += chr(i)

print(string.format(string), end="")
