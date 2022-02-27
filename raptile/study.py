import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'


# Tag 有两个很重要的属性，name 和 attributes。
# 以直接通过点属性的方法来获取 Tag，但是这种方法只能获取第一个标签。同时我们可以多次调用点属性这个方法，来获取更深层次的标签。
def get_tag():
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    print(soup.prettify())
    div = soup.div.div
    print(div.name)
    print(div.attrs)


def get_id():
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    a = soup.find('a', attrs={'class': 'jump-link'})
    print(a.get('href'))
    print(a.get_text())
    print(a.prettify())


def select_aa():
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    a = soup.select('#close-python-network > span')
    print(a[0].get('href'))
    print(a[0].get('title'))
    print(a[0].contents)


if __name__ == '__main__':
    select_aa()
