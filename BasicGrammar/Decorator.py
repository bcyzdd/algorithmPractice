#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/11 15:37 
# ide： PyCharm
# file： Decorator.py
"""
装饰器
意图：
动态地给一个对象添加一些额外的职责。就增加功能来说，Decorator 模式相比生成子类更为灵活。
适用性：
 在不影响其他对象的情况下，以动态、透明的方式给单个对象添加职责。
 处理那些可以撤消的职责。
当不能采用生成子类的方法进行扩充时。一种情况是，可能有大量独立的扩展，为支持每一种组合将产生大量的子类，使得子类数目呈爆炸性增长。
另一种情况可能是因为类定义被隐藏，或类定义不能用于生成子类。
"""

import time
from functools import wraps


def running_time(func):
    """内部有新函数"""

    @wraps(func)
    def print_running_time(*args):
        """打印函数运行时间"""
        t0 = time.time()
        result = func(*args)
        need_time = time.time() - t0
        print('新列表生成时间（秒）：{:.8f}'.format(need_time))
        return result

    return print_running_time


@running_time
def new_list(n):
    """生成一个新的列表"""
    temp_list = []
    for x in range(n):
        temp_list.append(x * (x + 1))
    return temp_list


if __name__ == '__main__':
    print('新列表长度:{}'.format(len(new_list(1000000))))
    print('new_list 函数的 __name__ 属性：{}'.format(new_list.__name__))
    print('new_list 函数的 __doc__ 属性：{}'.format(new_list.__doc__))
