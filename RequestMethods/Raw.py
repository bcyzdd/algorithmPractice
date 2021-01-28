# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 11:13
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : TextHtml.py
# @Software: PyCharm
"""
（3）请求正文是raw
形式：
传入xml格式文本
    requests.post(url='',data='<?xml ?>',headers={'Content-Type':'text/xml'})
传入json格式文本
    requests.post(url='',data=json.dumps({'key1':'value1','key2':'value2'}),headers={'Content-Type':'application/json'})
或者
    requests.post(url='',json={{'key1':'value1','key2':'value2'}},headers={'Content-Type':'application/json'})
可以将一json串传给requests.post()的data参数，
"""

import requests
import json


def my_request():
    url = 'http://httpbin.org/post'
    headers = {'Content-Type': 'text/xml'}
    s = '<?xml ?>'
    
    r = requests.post(url, data=s, headers=headers)
    print(r.text)
    """
    # xml = "my xml"
    headers = {'Content-Type': 'application/xml'}
    requests.post('http://www.example.com', data=xml, headers=headers)
    或者把xml作为一个文件来传输：
    import requests
    
    def request_ws(request):
    with open(archivo_request,"r") as archivo:
        request_data = archivo.read()
    
    target_url = "http://127.0.0.1:8000/?wsdl"
    
    headers = {'Content-type':'text/xml'}
    
    data_response = requests.post(target_url, data=request_data, headers=headers)
    """


def my_request2():
    url = 'http://httpbin.org/post'
    headers = {'Content-Type': 'application/json'}
    s = json.dumps({'key1': 'value', 'key2': 'value2'})
    
    r = requests.post(url, data=s, headers=headers)
    print(r.text)
    """
    url = 'http://www.example/post'
    s = json.dumps({'key1': 'value1', 'key2': 'value2'})
    r = requests.post(url, data=s)
    print (r.text)
    区别：

    这里我们可以发现Requests模拟post请求时，请求头格式为application/x-www-form-urlencoded与application/json的主要差别
    在于请求主体的构造格式（前者是键值对，后者是JSON串）,
    前者直接用字典传入，
    后者用json.dumps()函数将字典转为JSON串即可。
    """


def my_request3():
    url = 'http://httpbin.org/post'
    headers = {'Content-Type': 'application/json'}
    s = {'key1': 'value1', 'key2': 'value2'}
    
    r = requests.post(url, data=s, headers=headers)
    print(r.text)


if __name__ == '__main__':
    my_request()
    print('=' * 50)
    my_request2()
    print('=' * 10)
    my_request3()

"""
{
  "args": {},
  "data": "<?xml ?>",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "8",
    "Content-Type": "text/xml",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-601233f4-41b1eab41672a39f53b3d6ac"
  },
  "json": null,
  "origin": "58.33.40.178",
  "url": "http://httpbin.org/post"
}

==================================================
{
  "args": {},
  "data": "{\"key1\": \"value\", \"key2\": \"value2\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "35",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-601233f5-6eb21e654cbb5b8c073862ba"
  },
  "json": {
    "key1": "value",
    "key2": "value2"
  },
  "origin": "58.33.40.178",
  "url": "http://httpbin.org/post"
}

==========
{
  "args": {},
  "data": "key1=value1&key2=value2",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "23",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-601233f5-7c1645e979b9b32f18c7d63e"
  },
  "json": null,
  "origin": "58.33.40.178",
  "url": "http://httpbin.org/post"
}
"""
