# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 19:05
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : insert_sort.py
# @Software: PyCharm


def insert_sort(data):
    for i in range(1, len(data)):
        tmp = data[i]
        for j in range(i, -1, -1):
            if tmp < data[j - 1]:
                data[j] = data[j - 1]
            else:
                break
        data[j]=tmp
    return i


if __name__ == '__main__':
    import random
    
    data = list(range(30))
    random.shuffle(data)
    print('before',data)
    num = insert_sort(data)
    print('after',data)
    print('循环次数',num)