# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 15:35
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : heap_sort.py
# @Software: PyCharm
"""
堆排序
堆定义：本质是一个完全二叉树，如果根节点的值是所有节点的最小值称为小根堆，如果根节点的值是所有节点的最大值，称为大根堆。

效率：O(nlogn)

原理：

将待排序数据列表建立成堆结构(建立堆)；
通过上浮(shift_up)或下沉(shift_down)等操作得到堆顶元素为最大元素（已大根堆为例）；
去掉堆顶元素，将最后的一个元素放到堆顶，重新调整堆，再次使得堆顶元素为最大元素（相比第一次为第二大元素）；
重复3操作，直到堆为空，最后完成排序；

"""


def sift(data, low, high):
    """
    调整堆函数
    :param data:待排序的数据列表
    :param low: 值较小的节点位置，可以理解未根节点
    :param high: 值较大的节点位置
    :return:
    """
    i = low
    j = 2 * i  # 父节点i所对应的左孩子
    tmp = data[i]  # 最较小节点的值
    while j <= high:
        if j < high and data[j] < data[j + 1]:  # 如果右孩子比左孩子大则把j指向右节点
            j += 1  # 指向右节点
        if tmp < data[j]:  # 如果此时位置较小的节点值比该节点值小，则将该节点上浮最为新的父节点，并调整该节点双亲
            data[i] = data[j]
            i = j  # 调整该节点的双亲的位置
            j = 2 * i
        else:
            break  # 否则代表本次调整已经完成，并且节点i已经无值
    data[i] = tmp  # 最后将被调整节点的值放到i节点上（空出的位置）


def heap_sort(data):
    """
    堆排序
    :param data:待排序的数据列表
    :return:
    """
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
    # 构建堆
    for i in range(n - 1, -1, -1):  # 调整过程，从最后一个元素开始交换
        data[0], data[i] = data[i], data[0]  # 交换
        sift(data, 0, i - 1)  # 开始调整


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre', data_list)
    heap_sort(data_list)
    print('after', data_list)
