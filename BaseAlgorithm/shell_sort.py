# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 16:02
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : shell_sort.py
# @Software: PyCharm
"""
希尔排序
效率：与增量有关，O(n1+￡)其中<0￡<1,如增量为2k-1 复杂度为O(n3/2)

原理：

先取一个小于n的整数d1作为第一个增量，把文件的全部记录分组。所有距离为d1的倍数的记录放在同一个组中。
先在各组内进行直接插入排序；
取第二个增量d2<d1重复上述的分组和排序，直至所取的增量  =1(  <  …<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。
"""


def shell_sort(data):
    d1 = len(data)  # 设置分割大小为d1，
    while d1 > 0:
        for i in range(d1, len(data)):
            tmp = data[i]  # 当前分割元素位置
            j = i - d1  # 上一个分割元素位置
            while j >= 0 and tmp < data[j]:  # 上一个元素分割位置比当前分割位置要大，则需要调整位置
                data[j + d1] = data[j]  # 后移动当前分割元素位置
                j -= d1  # 往前移d1
            data[j + d1] = tmp
        d1 //= 2  # 继续分割


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre', data_list)
    shell_sort(data_list)
    print('after', data_list)
