# -*- coding: utf-8 -*-
# @Time    : 2021/1/15 19:32
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : overloading.py
# @Software: PyCharm
"""
重载实例
"""


class Iphone:
    def unlock(self, pass_code, **kwargs):
        print('解锁iPhone，使用passcode')
        return True


class Iphone5s(Iphone):
    def _unlock_by_finger(self, fingerprint):
        if fingerprint:
            return True
        else:
            return False
    
    def unlock(self, pass_code, **kwargs):
        fingerprint = kwargs.get('fingerprint', None)
        if self._unlock_by_finger(fingerprint):
            print('通过指纹解锁')
            return True
        else:
            return super().unlock(pass_code)


class IphoneX(Iphone5s):
    def _unlock_by_face_id(self, face_id):
        if face_id:
            return True
        else:
            return False
    
    def unlock(self, pass_code, **kwargs):
        face_id = kwargs.get('face_id', None)
        fingerprint = kwargs.get('fingerprint', None)
        
        if self._unlock_by_face_id(face_id):
            print('通过人脸解锁')
            return True
        elif super().unlock(pass_code, fingerprint=fingerprint):
            return True
        else:
            return super().unlock(pass_code)


if __name__ == '__main__':
  
    your_phone = IphoneX()
    
    your_phone.unlock(pass_code=123456, fingerprint=888888)
    your_phone.unlock(pass_code=123456, face_id=888888)
    your_phone.unlock(pass_code=123456, xxx=888888)
