# -*- coding: utf-8 -*-
# @Time    : 2021/1/7 19:04
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : bubble_sort.py
# @Software: PyCharm
"""
冒泡排序
"""


def bubble_sort_optimization(data):
    for i in range(len(data) - 1):
        exchange = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                exchange = True
        if not exchange:
            break
    return i


if __name__ == '__main__':
    import random
    
    data = list(range(30))
    random.shuffle(data)
    print('pre', data)
    num = bubble_sort_optimization(data)
    
    print('after', data,'执行了{}次'.format(num))
