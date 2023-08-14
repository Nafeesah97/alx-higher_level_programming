#!/usr/bin/env python3

def no_c(my_string):
    if 'c' in my_string or 'C' in my_string:
        new_string = ''
        for ch in my_string:
            if ch != 'c' and ch != 'C':
                new_string += ch
        return new_string
