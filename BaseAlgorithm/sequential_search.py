# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:33
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : sequential_search.py
# @Software: PyCharm
"""
1.顺序查找

当数据存储在诸如列表的集合中时，我们说这些数据具有线性或顺序关系。
每个数据元素都存储在相对于其他数据元素的位置。 由于这些索引值是有序的，我们可以按顺序访问它们。
这个过程产实现的搜索即为顺序查找。

顺序查找原理剖析：从列表中的第一个元素开始，
我们按照基本的顺序排序，简单地从一个元素移动到另一个元素，直到找到我们正在寻找的元素或遍历完整个列表。
如果我们遍历完整个列表，则说明正在搜索的元素不存在。

代码实现：该函数需要一个列表和我们正在寻找的元素作为参数，并返回一个是否存在的布尔值。
found 布尔变量初始化为 False，如果我们发现列表中的元素，则赋值为 True。
"""


def search(alist, item):
    find = False
    cur = 0
    while cur < len(alist):
        if alist[cur] == item:
            find = True
            break
        else:
            cur += 1
    return find
