#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    total_nums = 0

    for num in uniq_list:
        total_nums += num

    return total_nums
