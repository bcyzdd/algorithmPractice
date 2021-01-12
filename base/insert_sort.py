# -*- coding: utf-8 -*-
# @Time    : 2021/1/4 10:35
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : insert_sort.py
# @Software: PyCharm
"""
插入排序
效率：O(n2)

原理：

以从小到大排序为例，元素0为第一个元素，插入排序是从元素1开始，尽可能插到前面。
插入时分插入位置和试探位置，元素i的初始插入位置为i，试探位置为i-1，
在插入元素i时，依次与i-1,i-2······元素比较，
如果被试探位置的元素比插入元素大，那么被试探元素后移一位，元素i插入位置前移1位，
直到被试探元素小于插入元素或者插入元素位于第一位。
重复上述步骤，最后完成排序
"""


def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        for j in range(i, -1, -1):
            # print('j当前取值',j)
            if tmp < data[j - 1]:
                data[j] = data[j - 1]
            else:
                break
        data[j] = tmp
    return i


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    print('pre', data_list)
    num = insert_sort(data_list) + 1
    print('after', data_list, '比较次数', num)
