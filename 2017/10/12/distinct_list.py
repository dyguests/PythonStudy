# -*- coding: utf-8 -*-


def distinct_list(lis):
    i = 0
    while i < len(lis):
        j = i + 1
        while j < len(lis):
            if lis[i] == lis[j]:
                del lis[j]
            else:
                j += 1
        i += 1


l = [1, 2, 3, 5, 4, 3, 2, 1, 6, 7, 3, 2, 1, 2, 4, 7]
print(l)
distinct_list(l)
print(l)

# [1, 2, 3, 5, 4, 3, 2, 1, 6, 7, 3, 2, 1, 2, 4, 7]
# [1, 2, 3, 5, 4, 6, 7]
