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
        print('mid 执行完成后的 data:', data)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


def partition(data, left, right):
    tmp = data[left]
    print('tmp:',tmp)
    i = 1
    while left < right:
        print('执行第{}次大循环'.format(i))
        print('left:{},right:{}'.format(left,right))
        
        n = 1
        while left < right and data[right] >= tmp:
            print('比较右边的值，执行第{}次循环'.format(n))
            print('data[right]{} >= tmp{}'.format(data[right],tmp))
            right -= 1
            n+=1
            print('right:',right)

        data[left] = data[right]
        print('右边的值比较完成后，data[left]:{},data[right]:{}'.format(data[left],data[right]))
        
        n = 1
        while left < right and data[left] <= tmp:
            print('比较左边的值，执行第{}次循环'.format(n))
            print('data[left]{} <= tmp {}:'.format(data[left],tmp))
            left += 1
            n += 1
            print('left',left)
        
        data[right] = data[left]
        print('左边的值比较完成后，data[right]:{},data[left]:{}'.format(data[right], data[left]))
        i+=1
        
    print('大循环结束后，data[left]:{},tmp:{}'.format(data[left],tmp))
    data[left] = tmp
    print('left',left)
    return left


if __name__ == '__main__':
    import random
    
    data_list = list(range(5))
    random.shuffle(data_list)
    
    print('pre', data_list)
    quick_sort(data_list, left=0, right=len(data_list) - 1)
    # print('after', data_list)
