# -*- coding: utf-8 -*-


def print_list_str(n: int):
    list_str = ''
    for i in range(1, n):
        list_str += str(i) + ','
    list_str += str(n)
    print(list_str)


print_list_str(20)
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
