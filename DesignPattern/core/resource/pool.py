# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 14:23
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : pool.py
# @Software: PyCharm
import os
import json
import time


class ResourcePool:
    """
    资源池类，负责资源的序列化和反序列化，已存储和读取
    """
    
    def __init__(self):
        self.topology = dict()  # 拓扑结构 用于存储测试资源实例
        self.information = dict()  # 用于存储描述资源池本身的信息
        self.reserved = None  # 存放占用者信息
        self.file_name = None
        self.owner = None
    
    def reserve(self):
        if self.file_name is None:
            raise Exception('load a resource file first')
        self.load(self.file_name, self.owner)
        self.reserved = {
            'owner': self.owner,
            'date': time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        }
        self.save(self.file_name)
    
    def add_device(self, device_name, **kwargs):
        if device_name in self.topology:
            raise Exception(f'device {device_name} already exists')
        self.topology[device_name] = ResourceDevice(device_name)
    
    def load(self, filename, owner):
        # 检查文件是否存在
        if not os.path.exists(filename):
            raise Exception(f'Cannot find file {filename}')
        self.file_name = filename
        
        # 初始化
        self.topology.clear()
        self.reserved = False
        self.information = dict()
        
        # 读取测试资源配置的json字符串
        with open(filename) as file:
            json_object = json.load(file)
            # 判断是否被占用
            if 'reserved' in json_object and json_object['reserved']['owner'] != owner:
                raise Exception(f"Resource is reserved by {json_object['reserved']['owner']}")
            self.owner = owner
        
        if 'info' in json_object:
            self.information = json_object['info']
        for key, value in json_object['devices'].items():
            device = ResourceDevice.from_dict(value)
            self.topology[key] = device
        
        # 映射所有设备的连接关系
        for key, device in json_object['devices'].items():
            for port_name, port in device['ports'].items():
                for remote_port in port['remote_ports']:
                    remote_port_obj = self.topology[remote_port['device']].ports[remote_port['port']]
                    self.topology[key].ports[port_name].remote_ports.append(remote_port_obj)
    
    def save(self, filename):
        with open(filename, mode='w') as file:
            root_object = dict()
            root_object['devices'] = dict()
            root_object['info'] = self.information
            for device_key, device in self.topology.items():
                root_object['devices'][device_key] = device.to_dict()
            json.dump(root_object, file, indent=4)
    
    def collect_device(self, device_type, count):
        ret = list()
        for key, value in self.topology.items():
            if value.type == device_type:
                ret.append(value)
            if len(ret) >= count:
                return ret
    
    def collect_all_device(self, device_type):
        ret = list()
        for key, value in self.topology.items():
            if value.type == device_type:
                ret.append(value)
        return ret


class ResourceDevice:
    """
    代表所有测试资源设备的配置类，字段动态定义
    """
    
    def __init__(self, name='', *args, **kwargs):
        self.name = name
        self.type = kwargs.get('type', None)
        self.description = kwargs.get('description', None)
        self.ports = dict()
    
    def add_port(self, name, *args, **kwargs):
        if name in self.ports:
            raise Exception(f'Port name {name} already exists')
        self.ports[f'{name}'] = DevicePort(self, name, args, kwargs)
    
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
    
    @staticmethod
    def from_dict(dic_obj):
        """
        反序列化方法
        :param dic_obj:
        :return:
        """
        ret = ResourceDevice()
        for key, value in dic_obj.items():
            if key == 'ports':
                ports = dict()
                for port_name, port in value.items():
                    ports[port_name] = DevicePort.from_dict(port, ret)
                setattr(ret, 'ports', ports)
            else:
                setattr(ret, key, value)
        return ret


class DevicePort:
    """
    代表设备的链接端口
    """
    
    def __init__(self, parent_device=None, name='', *args, **kwargs):
        self.parent = parent_device
        self.name = name
        self.description = kwargs.get('description', None)
        self.remote_ports = list()
    
    def to_dict(self):
        """
        序列化，方便信息转为json，存入文件
        :return:
        """
        ret = dict()
        for key, value in self.__dict__.items():
            if key == 'parent':
                ret[key] = value.name
            elif key == 'remote_ports':
                ret[key] = list()
                for remote_port in value:
                    # 使用device的名称和port的名称来标示远端的端口
                    # 在反序列化的时候可以方便地找到对应的对象实例
                    ret[key].append((
                        {
                            'device': remote_port.parent.name,
                            'port': remote_port.name,
                        }
                    ))
            else:
                ret[key] = value
        return ret
    
    @staticmethod
    def from_dict(dict_obj, parent):
        """
        反序列化为实例，方便调用
        返回一个DevicePort的实例
        :param dict_obj:
        :param parent:
        :return:
        """
        ret = DevicePort(parent)
        for key, value in dict_obj.items():
            if key == 'remote_ports' or key == 'parent':
                continue
            setattr(ret, key, value)  # 通过setattr将原本没有定义在DevicePort类中的属性添加进去
        return ret


if __name__ == '__main__':
    switch1 = ResourceDevice(name='switch1')
    switch1.add_port('ETH1/1')
    switch1.add_port('ETH1/2')
    
    switch2 = ResourceDevice(name='switch2')
    switch2.add_port('ETH1/1')
    switch2.add_port('ETH1/2')
    
    switch1.ports['ETH1/1'].remote_ports.append(switch2.ports['ETH1/1'])
    switch2.ports['ETH1/1'].remote_ports.append(switch1.ports['ETH1/1'])
    
    print(switch1.to_dict())
    print(switch2.to_dict())
    
    rp = ResourcePool()
    rp.topology['switch1'] = switch1
    rp.topology['switch2'] = switch2
    rp.save('test.json')
    info = rp.load('test.json')
    print('done')
