#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# datetime： 2021/5/7 18:43 
# ide： PyCharm
# file： bubble_sort.py
"""
冒泡排序
"""


def bubble_sort(param):
    for i in range(len(param) - 1):
        for j in range(len(param) - i - 1):
            if param[j] > param[j + 1]:
                param[j], param[j + 1] = param[j + 1], param[j]


if __name__ == '__main__':
    import random

    data = list(range(30))
    random.shuffle(data)

    print('pre', data)
    bubble_sort(data)
    print('after', data)
