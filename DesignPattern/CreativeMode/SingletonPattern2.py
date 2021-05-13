#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/13 12:43 
# ide： PyCharm
# file： SingletonPattern2.py
"""
单例模式
"""

from threading import Thread, Lock


class Singleton:
    """
    线程安全的单例模式
    """
    _instance_lock = Lock()
    _init_lock = Lock()

    def __new__(cls, *args, **kwargs):
        with Singleton._instance_lock:
            if not hasattr(Singleton, '_instance'):
                print('first new')
                Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self):
        with Singleton._init_lock:
            if not hasattr(Singleton, '_first_init'):
                print('first init')
                Singleton._first_init = True


def task(i):
    obj = Singleton()
    print(f'Thread-{i}:{obj}')


if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task, args=(i,))
        t.start()
