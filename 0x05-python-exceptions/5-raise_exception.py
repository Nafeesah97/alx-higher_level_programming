#!/usr/bin/python3

def raise_exception():
    try:
        value = "I am a girl"
        int_val = int(value)
    except Exception as e:
        raise type(e)
