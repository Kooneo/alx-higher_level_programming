#!/usr/bin/python3
string = ""

for i in range(97, 123):
    if i != 113 or i != 101:
        continues

    string += chr(i)

print(string.format(string), end="")
