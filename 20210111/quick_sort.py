# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 20:42
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : quick_sort.py
# @Software: PyCharm
"""
效率:平均O(nlogn)

原理：

从数列中随机挑选出一个数作为基数；
重新排列数列，使得比基数小的元素在左边，比基数大元素在右边，相等的元素放左边或者右边都可以，
最后使得该基数在处于数列中间位置，这个称为分区操作；
递归上述操作，完成排序，如下如；

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
    
    print('pre', data_list)
    quick_sort(data_list, left=0, right=len(data_list) - 1)
    print('after', data_list)
