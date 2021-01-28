# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 11:12
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : MultipartFormData.py
# @Software: PyCharm
"""
2、multipart/form-data
这又是一个常见的 POST 数据提交的方式。我们使用表单上传文件时，必须让 form 的 enctyped 等于这个值，下面是示例

    POST http://www.example.com HTTP/1.1
    Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryrGKCBY7qhFd3TrwA
    ------WebKitFormBoundaryrGKCBY7qhFd3TrwA
    Content-Disposition: form-data; name="text"
    title
    ------WebKitFormBoundaryrGKCBY7qhFd3TrwA
    Content-Disposition: form-data; name="file"; filename="chrome.png"
    Content-Type: image/png
    PNG ... content of chrome.png ... ------WebKitFormBoundaryrGKCBY7qhFd3TrwA--
"""
import requests
from requests_toolbelt import MultipartEncoder


def my_request():
    """
        （2）请求正文是multipart/form-data
        除了传统的application/x-www-form-urlencoded表单，
        我们另一个经常用到的是上传文件用的表单，这种表单的类型为multipart/form-data。
        requests.post(url='',data={'key1':'value1','key2':'value2'},
        headers={'Content-Type':'multipart/form-data'})
    :return:
    """
    m = MultipartEncoder(
        fields={
            'field0': 'value',
            'field1': 'value',
            'field2': ('filename', open('file.py', 'rb'), 'text/plain')
        }
    )
    r = requests.post('http://httpbin.org/post', data=m, headers={'Content-Type': m.content_type})
    print(r.text)


def my_request2():
    m = MultipartEncoder(fields={'field0': 'value', 'field2': 'value'})
    
    r = requests.post('http://httpbin.org/post', data=m, headers={'Content-Type': m.content_type})
    print(r.text)
    """
    （四）multipart/form-data数据格式
        除了传统的application/x-www-form-urlencoded表单，我们另一个经常用到的是上传文件用的表单，
        这种表单的类型为multipart/form-data，
        multipart/form-data主要用于文件上传，当我们使用它时，必须让 form表单的enctype 等于 multipart/form-data
        直接来看一个请求示例，主要：
        请看代码(实现上传本地的test.txt文件)：
        
        import requests
        files = {"file": open("C:/Users/Administrator/Desktop/test.txt", "rb")}
        r = requests.post("http://httpbin.org/post", files=files)
        print(r.text)
    """


def my_request3():
    import requests
    import json
    # 设置URL
    url = "http://demo.9meikf.cn/usystem/auto/getAnswer.do"
    # 设置消息头
    headers = {
        "Cookie": "JSESSIONID=EA01FF2B025861F39E29712C97F7DF69;CASTGC=TGT-136-bLQMf0CAikK4BGaydOfIeKd6tWpZQEznJ2ZWdcVl9ofI4LiaQb-cas01.example.org",
        "Content-Type": "application/json"
    }
    # 设置消息体
    data = {"companyId": "48622",
            "nodeId": 6,
            "question": "不需要",
            "templateId": "c6f5ad67fc2c11e8a11800163e086942"}
    # 获取相应
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print("Status code:", response.status_code)
    print(response.text)
    # 解析相应
    info = response.json()
    # 验证数据
    assert str(info['answer']) == 'reject'


if __name__ == '__main__':
    my_request2()

"""
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "field0": "value",
    "field2": "value"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "222",
    "Content-Type": "multipart/form-data; boundary=b5e70283711944c285c15ae38e03a300",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-60123113-67a2b6cf65e0e33f575d4cb3"
  },
  "json": null,
  "origin": "58.33.40.178",
  "url": "http://httpbin.org/post"
}
"""
