# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 19:16
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : quick_sort.py
# @Software: PyCharm
"""
快排默写
"""


def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


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


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre',data_list)
    quick_sort(data_list,left=0,right=len(data_list)-1)
    print('after',data_list)
