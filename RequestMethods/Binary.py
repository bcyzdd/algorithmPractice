# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 11:49
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : Binary.py
# @Software: PyCharm
"""
（4）请求正文是binary
形式：
requests.post(url='',files={'file':open('test.xls','rb')},headers={'Content-Type':'binary'})
Requests也支持以multipart形式发送post请求，只需将一文件传给requests.post()的files参数即可。
"""
import requests


def my_request():
    url = 'http://httpbin.org/post'
    files = {'file': open('report.txt', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)


if __name__ == '__main__':
    my_request()

"""
{
  "args": {},
  "data": "",
  "files": {
    "file": "Hello world!"
  },
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "158",
    "Content-Type": "multipart/form-data; boundary=8d6c87d03bc7d79f790b45014bba0446",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-6012348a-0b64f17562119865339ad844"
  },
  "json": null,
  "origin": "58.33.40.178",
  "url": "http://httpbin.org/post"
}

"""
