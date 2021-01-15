# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:35
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
    """
    快速排序
    :param data:数据列表
    :param left: 基准数左边元素索引
    :param right: 基准数右边元素索引
    :return:
    """
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)  # 对基准数前面进行排序
        quick_sort(data, mid + 1, right)  # 对基准数前面进行排序


def partition(data, left, right):
    tmp = data[left]  # 随机选择的基准数，从最左边开始选择
    while left < right:
        while left < right and data[right] >= tmp:  # 右边的数比基准数大
            right -= 1  # 保留该数，然后索引指针左移
        data[left] = data[right]  # 否则此时右边比基数小，则将该数据放在基准位置
        while left < right and data[left] <= tmp:  # 左边的数比基准小
            left += 1  # 此时保持该数位置不变，索引前移
        data[right] = data[left]  # 否则此时左边的数比基数大，则将该数放在右边
    data[left] = tmp  # 最后基准数放回中间
    print(left)
    return left  # 返回基准数位置


if __name__ == '__main__':
    import random
    
    data_list = list(range(10))
    random.shuffle(data_list)
    print('pre', data_list)
    quick_sort(data_list, 0, len(data_list) - 1)
    print('after', data_list)
