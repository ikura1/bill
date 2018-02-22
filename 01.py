# -*- coding: utf-8 -*-
def deco_print_log(name):
    def _print_log(func):
        def print_log(*attr):
            print(name, ':', attr)
            result = func(*attr)
            print('結果', result)
            return result
        return print_log
    return _print_log


@deco_print_log('del')
def del_water(youki):
    youki[1] = 0
    return youki


@deco_print_log('add')
def add_water(youki, mizu):
    youki[1] += mizu
    if youki[1] >= youki[0]:
        youki[1] = youki[0]
    return youki


@deco_print_log('move')
def move_youki(i, j):
    i[1] += j[1]
    if i[1] <= i[0]:
        j[1] = 0
    else:
        sa = i[1] - i[0]
        i[1] = i[0]
        j[1] = sa
    return i, j


a = [3, 0]
b = [5, 0]
a = add_water(a, 10)
b, a = move_youki(b, a)
a = add_water(a, 10)
b, a = move_youki(b, a)
b = del_water(b)
b, a = move_youki(b, a)
a = add_water(a, 10)
b, a = move_youki(b, a)
print('結果: ', b[1])
