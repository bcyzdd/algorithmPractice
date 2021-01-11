# -*- coding: utf-8 -*-
# @Time    : 2021/1/5 9:44
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : bubble_sort.py
# @Software: PyCharm
"""
冒泡排序
"""


def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


if __name__ == '__main__':
    import random
    
    data = list(range(30))
    random.shuffle(data)
    
    print('pre',data)
    bubble_sort(data)
    print('after',data)