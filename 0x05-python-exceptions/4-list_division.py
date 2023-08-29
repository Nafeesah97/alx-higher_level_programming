#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    try:
        for i, j in zip(my_list_1, my_list_2):
            try:
                res = i / j

            except TypeError:
                res = 0
                print("wrong type")
            except IndexError:
                res = 0
                print("out of range")
            except ZeroDivisionError:
                res = 0
                print("division by 0")
            else:
                res_list.append(res)
    except Exception:
        pass
    finally:
        if len(res_list) < list_length:
            print("out of range")
            res_list.extend([0] * (list_length - len(res_list)))
        return res_list[:list_length]
