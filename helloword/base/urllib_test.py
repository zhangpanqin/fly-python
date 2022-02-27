from urllib import request
from urllib.request import urlopen


def test1():
    response = urlopen("http://www.python.org")
    print(response.read())


def test3():
    url = 'http://www.python.org'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    req = request.Request(url, headers=headers, method='GET')
    response = request.urlopen(req)
    print(response.read())


if __name__ == '__main__':
    test3()
