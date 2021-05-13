#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/13 13:04 
# ide： PyCharm
# file： AbstractFactory.py
"""
3. 抽象工厂模式
工厂方法虽然方便了我们以后的扩展，但如果我们要生产很多不同产品，就同样需要写很多对应的工厂类。
为了解决这个问题，我们需要把同类产品进一步抽象到一个工厂类中，这就是抽象工厂。

简单工厂模式：允许固定接口创建对象，用户只关心哪种类型的实例被创建，不必关心其初始化过程。
工厂方法模式：在简单工厂的优点上进行改进，将具体得创建工作交给相应子类去做，使得系统更高效扩展。
抽象工厂模式：在工厂方法的基础上扩展了一个工厂对多个产品创建的支持。
三种工厂模式复杂度逐步递增，实际使用过程中，应根据系统复杂度采用合适的工厂模式。
"""


class Benz_C63:
    def __repr__(self):
        return 'This is Benz-C63'


class BMW_M3:
    def __repr__(self):
        return 'This is BMW-M3'


class Benz_G63:
    def __repr__(self):
        return 'This is Benz-G63'


class BMW_X5:
    def __repr__(self):
        return 'This is BMW-X5'


class AbsFactory:
    """
    抽象工厂
    可以生产不同的车型：小轿车、SUV
    """

    def produce_car(self):
        pass

    def produce_suv(self):
        pass


class BenzFactory(AbsFactory):
    def produce_car(self):
        return Benz_C63()

    def produce_suv(self):
        return Benz_G63()


class BMWFactory(AbsFactory):
    def produce_car(self):
        return BMW_M3()

    def produce_suv(self):
        return BMW_X5()


def main():
    """
    我们可以通过特定的工厂来获得特定的产品
    :return:
    """

    car1 = BenzFactory().produce_car()
    car2 = BMWFactory().produce_car()
    suv1 = BenzFactory().produce_suv()
    suv2 = BMWFactory().produce_suv()
    print(f'car1: {car1}')
    print(f'car2: {car2}')
    print(f'suv1: {suv1}')
    print(f'suv2: {suv2}')


if __name__ == '__main__':
    main()
