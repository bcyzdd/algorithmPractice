# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:34
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : bubble_sort.py
# @Software: PyCharm
"""
冒泡排序
效率：O(n2)

原理：

比较相邻的元素，如果第一个比第二个大，就交换他们两个；
对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。做完以后，最后的元素会是最大的数，这里可以理解为走了一趟；
针对所有的元素重复以上的步骤，除了最后一个；
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较，最后数列就是从大到小一次排列；

参见
https://www.cnblogs.com/wdliu/p/9481122.html

"""


def bubble_sort(data):
    for i in range(len(data) - 1):  # 趟数
        for j in range(len(data) - 1 - i):  # 遍历数据，依次交换
            if data[j] > data[j + 1]:  # 当较大的数再前面
                data[j], data[j + 1] = data[j + 1], data[j]  # 交换两个数的位置


def bubble_sort_optimization(data):
    for i in range(len(data) - 1):
        exchange = False
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                exchange=True
        if not exchange:
            break
    return i


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre', data_list)
    bubble_sort(data_list)
    print('after', data_list)

    data_list2 = list(range(30))
    random.shuffle(data_list2)
    print('pre2', data_list2)
    num = bubble_sort_optimization(data_list2)+1
    print('after2', data_list,'比较次数',num)
    
    
