# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:33
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : binary_search.py
# @Software: PyCharm
"""
2.二分查找

有序列表
对于我们的实现搜索是很有用的。
在顺序查找中，当我们与第一个元素进行比较时，如果第一个元素不是我们要查找的，则最多还有 n-1 个元素需要进行比较。

二分查找则是从中间元素开始，而不是按顺序查找列表。 如果该元素是我们正在寻找的元素，我们就完成了查找。
如果它不是，我们可以使用列表的有序性质来消除剩余元素的一半。

如果我们正在查找的元素大于中间元素，就可以消除中间元素以及比中间元素小的一半元素。如果该元素在列表中，肯定在大的那半部分。
然后我们可以用大的半部分重复该过程，继续从中间元素开始，将其与我们正在寻找的内容进行比较。
"""


def search(alist, item):
    left = 0
    right = len(alist) - 1
    find = False
    
    while left <= right:
        mid_index = (left + right) // 2
        if item == alist[mid_index]:
            find = True
            break
        else:
            if item > alist[mid_index]:
                left = mid_index + 1
            else:
                right = mid_index - 1
    
    return find
