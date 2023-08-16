#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            j = 0
            while j < i:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                j += 1
        return my_list[-1]
