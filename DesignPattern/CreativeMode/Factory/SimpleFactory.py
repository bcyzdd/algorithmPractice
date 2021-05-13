#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/13 12:54 
# ide： PyCharm
# file： SimpleFactory.py
"""
工厂模式，就是我们可以通过一个指定的“工厂”获得需要的“产品”。
在这种模式中，用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象实例，
隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。

1. 简单工厂模式
"""


class Benz:
    def __repr__(self):
        return 'This is Benz'


class BMW:
    def __repr__(self):
        return 'This is BMW'


class CarFactory:
    def produce_car(self, typename):
        if typename == 'benz':
            return Benz()

        elif typename == 'bmw':
            return BMW()


def main():
    car_factory = CarFactory()
    car1 = car_factory.produce_car('benz')
    car2 = car_factory.produce_car('bmw')
    print(f'car1:{car1}')
    print(f'car2:{car2}')


if __name__ == '__main__':
    main()
