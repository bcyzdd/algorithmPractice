#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/10 19:00 
# ide： PyCharm
# file： insert_sort.py
"""
插入排序
"""


def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        for j in range(i, -1, -1):
            if tmp < data[j - 1]:
                data[j] = data[j - 1]
            else:
                break
        data[j] = tmp
    return i


if __name__ == '__main__':
    import random

    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre', data_list)
    num = insert_sort(data_list) + 1
    print('after', data_list, '比较次数', num)
