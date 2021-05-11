#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/11 14:47 
# ide： PyCharm
# file： DecoratorPattern.py
"""
装饰器模式
该模式虽名为修饰器，但这并不意味着它应该只用于让产品看起来更漂亮。
修饰器模式通常用于扩展一个对象的功能。这类扩展的实际例子有，给枪加一个消音器、使用不同的照相机镜头
"""

import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize
def nsum(n):
    """返回前n个数字之和"""
    assert (n >= 0), 'n must be >=0'
    return 0 if n == 0 else n + nsum(n - 1)


@memoize
def fibonacci(n):
    """返回斐波那契数列的第n个数"""
    assert (n >= 0), 'n must be >=0'
    return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # from timeit import Timer
    #
    # measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci',
    #             'func': fibonacci},
    #            {'exec': 'nsum(200)', 'import': 'nsum',
    #             'func': nsum}
    #            ]
    # for m in measure:
    #     print(m['exec'])
    #     print(m['import'])
    #     print(m['func'].__name__)
    #     print(m['func'].__doc__)
    #
    #     # t = Timer('{}'.format(m['exec'], 'from __main__ import {}'.format(m['import'])))
    #     # print('name :{},doc :{},executing:{},time:{}'.format(m['func'].__name__, m['func'].__doc__, m['exec'],
    #     #
    #     t.timeit()))
    print(nsum(10))
