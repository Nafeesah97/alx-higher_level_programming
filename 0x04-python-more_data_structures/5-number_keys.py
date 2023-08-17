#!/usr/bin/python3

def number_keys(a_dictionary):
    i = 0
    list_dic = []
    for k, v in a_dictionary.items():
        list_dic.append(k)
    return len(list_dic)
