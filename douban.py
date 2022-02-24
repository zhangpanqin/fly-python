#!/usr/bin/env python
# encoding=utf-8
"""
aaa
"""
import json
from os import getcwd


def jsonDemo():
    json_str = """
{
    "code": "200",
    "data": [
        {
            "create_time": "2小时前",
            "id": 3,
            "title": "对话董明珠：这个时代要倡导利他思想",
            "url": "https://www.thepaper.cn/newsDetail_forward_3131849"
        }
    ],
    "msg": "请求成功"
}
"""
    print(json.load(json_str).code)


def main():
    # data = requests.get('https://github.com/').content
    # print(data)
    print('当前目录' + getcwd())
    with open('README.md', 'r', encoding='UTF-8') as f:
        print(f.read())


if __name__ == '__main__':
    jsonDemo()
