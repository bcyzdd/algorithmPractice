#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/13 13:00 
# ide： PyCharm
# file： Factory.py
"""
2. 工厂方法模式
上面我们有了一个简单的工厂，但如果我们要新增一个产品奥迪汽车，除了要新增加一个Audi类之外，还要修改CarFactory中的produce_car方法，这样不利于以后的扩展。
所以我们在简单工厂的基础上，抽象出不同的工厂，每个工厂对应生产自己的产品，这就是工厂方法。
"""


class Benz:
    def __repr__(self):
        return 'This is Benz'


class BMW:
    def __repr__(self):
        return 'This is BMW'


class AbsFactory:
    def produce_car(self):
        pass  # 只定义了方法，并没有实现，具体功能在子类中实现


class BenzFactory(AbsFactory):
    def produce_car(self):
        return Benz()


class BMWFactory(AbsFactory):
    def produce_car(self):
        return BMW()


def main():
    """
    可以通过特定的工厂来获得特定的产品
    :return:
    """
    car1 = BenzFactory().produce_car()
    car2 = BMWFactory().produce_car()
    print(f'car1 :{car1}')
    print(f'car2 :{car2}')


if __name__ == '__main__':
    main()
