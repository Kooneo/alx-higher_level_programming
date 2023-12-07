#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(a_dictionary)
    for key, value in range(len(sorted_dic)):
        print("{}: {}".format(key, value))
