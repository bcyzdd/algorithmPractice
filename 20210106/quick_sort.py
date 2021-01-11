# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 17:48
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : quick_sort.py
# @Software: PyCharm
"""
快排
"""


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


if __name__ == '__main__':
    import random
    
    data = list(range(30))
    random.shuffle(data)
    print('pre', data)
    quick_sort(data, 0, len(data) - 1)
    print('after', data)
