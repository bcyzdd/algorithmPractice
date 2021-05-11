#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： bcy
# Email ： changyi.bu@linkedcare.cn
# datetime： 2021/5/11 15:10 
# ide： PyCharm
# file： FacadePattern.py
"""
外观模式
外观模式又叫做门面模式。在面向对象程序设计中，解耦是一种推崇的理念。但事实上由于某些系统中过于复杂，从而增加了客户端与子系统之间的耦合度。
例如：在家观看多媒体影院时，更希望按下一个按钮就能实现影碟机，电视，音响的协同工作，而不是说每个机器都要操作一遍。
这种情况下可以采用外观模式，即引入一个类对子系统进行包装，让客户端与其进行交互。

外观模式(Facade Pattern)：外部与一个子系统的通信必须通过一个统一的外观对象进行，为子系统中的一组接口提供一个一致的界面，
外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用。外观模式又称为门面模式，它是一种对象结构型模式。
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    """初始化文件服务器进程要求的操作"""

    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('boting the {}'.format(self))
        """启动文件服务器进程要求的操作"""
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        """终止文件服务器要求的操作"""
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        """
        检查访问的有效性、用户权限等
        :param user:
        :param name:
        :param permissions:
        :return:
        """
        print('trying to create the file "{}" for user "{}" with permissions {}'.format(name, user, permissions))


class ProcessServer(Server):
    def __init__(self):
        """初始化进程服务器要求的操作"""
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        """启动进程服务进程要去的操作"""
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        """终止进程服务进程要求的操作"""
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        """
        检查用户权限和生成PID等
        :param user:
        :param name:
        :return:
        """
        print('trying to crate the process "{}" for user "{}"'.format(name, user))


class WindowServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:
    """外观"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()
