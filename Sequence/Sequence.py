# -*- coding: utf-8 -*-
# @Time    : 2021/1/19 14:20
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : Sequence.py
# @Software: PyCharm
"""
将信息序列化和反序列化
目的：
    序列化   将测试信息保存成相应的文本文件
    反序列化 通过文本反序列化为测试信息的实例

例子
"""


class ResourceDevice:
    """
    代表所有测试资源设备的配置类，字段动态定义
    """
    
    def __init__(self, name="", *args, **kwargs):
        self.name = name
        self.type = kwargs.get('type', None)
        self.description = kwargs.get('description', None)
        self.ports = dict()
    
    def add_port(self, name, *args, **kwargs):
        if name in self.ports:
            raise Exception(f'Port name {name} already exists')
        self.ports[f'{name}'] = DevicePort(self.name, *args, **kwargs)
    
    def to_dict(self):
        ret = dict()
        for key, value in self.__dict__.items():
            if key == 'ports':
                ret[key] = dict()
                for port_name, port in value.items():
                    ret[key][port_name] = port.to_dict()
            else:
                ret[key] = value
        return ret


class DevicePort:
    """
    代表社保的连接端口
    """
    
    def __init__(self, parent_device=None, name="", *args, **kwargs):
        
        self.parent = parent_device
        self.name = name
        self.description = kwargs.get('description', None)
        self.remote_ports = list()
    
    def to_dict(self):
        ret = dict()
        for key, value in self.__dict__.items():
            if key == 'parent':
                ret[key] = value.name
            elif key == 'remote_ports':
                ret[key] = list()
                for remote_port in value:
                    ret[key].append(
                        {
                            'device': remote_port.parent.name,
                            'port': remote_port.name
                        }
                    )
            else:
                ret[key] = value
        return ret


if __name__ == '__main__':
    import json
    
    switch1 = ResourceDevice(name='switch')
    switch1.add_port('ETH/1')
    switch1.add_port('ETH/2')

    switch2 = ResourceDevice(name='switch')
    switch2.add_port('ETH/1')
    switch2.add_port('ETH/2')
    
    switch1.ports['ETH/1'].remote_ports.append(switch2.ports['ETH/1'])
    switch2.ports['ETH/1'].remote_ports.append(switch1.ports['ETH/1'])
    print(json.dumps(switch1.to_dict(),indent=4))
    
