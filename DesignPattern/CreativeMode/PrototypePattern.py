#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/11 13:55 
# ide： PyCharm
# file： PrototypePattern.py
"""
原型模式
用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象
原型模式本质就是克隆对象，所以在对象初始化操作比较复杂的情况下，
很实用，能大大降低耗时，提高性能，因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

浅拷贝（Shallow Copy）:指对象的字段被拷贝，而字段引用的对象不会被拷贝，拷贝的对象和源对象只是名称相同，但是他们共用一个实体。
深拷贝（deep copy）:对对象实例中字段引用的对象也进行拷贝。
"""
import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        """

        :param name:
        :param authors:
        :param price:
        :param rest: 出版商、长度、标签、出版日期等
        """
        self.name = name
        self.authors = authors
        self.price = price  # 单位为美元
        self.__dict__.update(rest)

    def __str__(self):
        pylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))

        for i in ordered.keys():
            pylist.append('{}:{}'.format(i, ordered[i]))
            if i == 'price':
                pylist.append('$')
            pylist.append('\n')
        return ''.join(pylist)


class Prototype:

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier:{}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book(name='The C Programming Language', authors=('Brian w.Ken', 'BCY'), price=119, publisher='新华社', length=228,
              publish_data='1988-09-22',
              tags=('C', 'programming', 'algorithms', 'data structures'))
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.98, length=273,
                         publish_data='2021-05-11', edition=2)

    for i in (b1, b2):
        print(i)

    print('ID b1 :{} != ID b2:{}'.format(id(b1), id(b2)))


if __name__ == '__main__':
    main()
