# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 20:35
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : quick_sort.py
# @Software: PyCharm
"""快速排序"""


def quick_sort(data, left, right):
    """
    
    :param data:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1) # 对基准数前面进行排序
        quick_sort(data, mid + 1, right)  # 对基准数前面进行排序


def partition(data, left, right):
    tmp = data[left] # 随机选择的基准数，从最左边开始选择
    
    while left < right:
        while left < right and data[right] >= tmp: # 右边的数比基准数大
            right -= 1 # 保留该数，然后索引指针左移
        data[left] = data[right] # 否则此时右边比基数小，则将该数据放在基准位置
        
        while left < right and data[left] <= tmp: # 左边的数比基准小
            left += 1  # 此时保持该数位置不变，索引前移
        data[right] = data[left]  # 否则此时左边的数比基数大，则将该数放在右边
    
    data[left] = tmp  # 最后基准数放回中间
    return left # 返回基准数位置


if __name__ == '__main__':
    import random
    
    data_list = list(range(30))
    random.shuffle(data_list)
    
    print('pre',data_list)
    quick_sort(data_list,left=0,right=len(data_list)-1)
    print('after',data_list)