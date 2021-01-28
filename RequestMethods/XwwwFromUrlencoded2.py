# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 11:21
# @Author  : bcy
# @Email   : buchangyi@yxqiche.com
# @File    : XwwwFromUrlencoded2.py
# @Software: PyCharm
"""
post请求四种传送正文方式：
　　（1）请求正文是application/x-www-form-urlencoded

　　（2）请求正文是multipart/form-data

　　（3）请求正文是raw

　　（4）请求正文是binary
"""


def my_request():
    """
    Reqeusts支持以form表单形式发送post请求，
    只需要将请求的参数构造成一个字典，
    然后传给requests.post()的data参数即可。
    requests.post(url='',data={'key1':'value1','key2':'value2'},
    headers={'Content-Type':'application/x-www-form-urlencoded'})
    :return:
    """
    import requests
    
    url = 'http://httpbin.org/post'
    d = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post(url, data=d)
    print(r.text)
    """
    datas = {'parameter1':'12345','parameter2':'23456'}
    r = requests.post('http://example.com',data=datas)
    print(r.content)
    print(r.status_code)
      解说：Reqeusts支持以application/x-www-form-urlencoded数据格式发送post请求，
      只需要将请求的参数构造成一个字典，然后传给requests.post()的data参数即可。
    """


def my_request2():
    import requests
    import json
    from urllib import parse
    
    # 定义请求header
    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', 'Key': '332213fa4a9d4288b5668ddd9'}
    # 定义请求地址
    url = "https://api.newrank.cn/api/sync/weibo/trend"
    # 通过字典方式定义请求body
    FormData = {"from": '2018-07-18 16:00:00', "to": '2018-07-18 18:00:00', "page": 1, "size": 1}
    # 字典转换k1=v1 & k2=v2 模式
    data = parse.urlencode(FormData)
    # 请求方式
    content = requests.post(url=url, headers=HEADERS, data=data).text
    content = json.loads(content)
    print(content)


if __name__ == '__main__':
    my_request()

"""
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "key1": "value1",
    "key2": "value2"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Length": "23",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.22.0",
    "X-Amzn-Trace-Id": "Root=1-60122e2f-1d599e170e065ec315751587"
  },
  "json": null,
  "origin": "58.33.40.178",
  "url": "http://httpbin.org/post"
}
"""
