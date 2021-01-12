# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:35
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : merge_sort.py
# @Software: PyCharm
"""
归并排序
效率：O(nlogn)

空间复杂度：O(n)

原理：

申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
设定两个指针，最初位置分别为两个已经排序序列的起始位置；
比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
重复步骤3直到某一指针达到序列尾；
将另一序列剩下的所有元素直接复制到合并序列尾。
"""


def merge(data, low, mid, high):
    """
    合并函数
    :param data:数据列表
    :param low:列表开头位置
    :param mid:分割中间位置
    :param high:列表最后位置
    :return:
    """
    i = low  # 第一个指针
    j = mid + 1  # 第二个指针
    tmp = []  # 临时存在的列表
    while i <= mid and j <= high:  # 分割的列表当两边都有数才进行
        if data[i] < data[j]:
            tmp.append(data[i])
            i += 1  # 低的指针往右移动
        else:
            tmp.append(data[j])  # 右边大，存右边的数
            j += 1  # 同时指针右移动
    while i <= mid:  # 左边分割有剩下
        tmp.append(data[i])
        i += 1
    while j <= high:  # 右边分割有剩下
        tmp.append(data[j])
        j += 1
    data[low:high + 1] = tmp  # 最后将tmp中的数写入到原来的列表中


def merge_sort(data, low, high):
    if low < high:  # 至少有两个元素才进行
        mid = (low + high) // 2  # 分割
        merge_sort(data, low, mid)  # 递归分割上一部分
        merge_sort(data, mid + 1, high)  # 递归分割下一部分
        merge(data, low, mid, high)  # 合并


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre', data_list)
    merge_sort(data_list, 0, len(data_list) - 1)
    print('after', data_list)
