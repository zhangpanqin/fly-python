## 基础

### 列表和元组

元组是不变的对象. 列表时可变对象.

```python
# 列表,类比 java 中 List
a = [1, 2, 3]
# 元组 类比 java 中 Array
b = (2, 3, 4)
```

### 字典和集合

字典是 key = value 格式,key 和 value 都是不可变对象.

```python
# 字典 ,类比 java 中 map
c = {'a': 1, 'b1': 22}
# 推荐这样获取,不存在的 key 不会报错,返回 None
print(c.get('a'))
# 这种不存在 key 会报错.
print(c['a'])

# 集合,类比 java 中 Set
d = {'a', 'b'}
d1 = 'abc123133'
d2 = set(d1)
print(d2)

print(d1 | d2)
print(d1 & d2)
print(d1 ^ d2)
```

### if

```python
if 1 > 0:
    print('aaa')
elif 2 > 0:
    print('ccc')
else:
    print('bbb')
```

### while

```python
a = 10
while a > 0:
    print('aaaa')
    a = -1
print('ccc')

```

### for

```python
string = '123456'
for a in string:
    print(a)

list = [1, 2, 3, 4]
for a in list:
    print(2)

arr = (1, 2, 3, 4)

for a in arr:
    print(a)

map = {'a': 1, 'b': 2}

for it in map:
    # 遍历 key
    print(it)

set2 = {'a', "b"}
for it in set2:
    print(it)

```

### 函数

```python
def demo(a, b='默认'):
    print('a=', a)
    print('b=', b)


demo('11', 'a')
demo(b='a', a='11')


# 可变参数
def demo2(*args):
    # 元组
    print(type(args))


def demo4(**kwargs):
    # 字典,map
    print(type(kwargs))
    print(kwargs)


# 必须带着变量
demo4(a=1, b=2)
```

### 作用域

参考 js 的作用域

```python
x = 2


def demo2():
    x = 10
    print(x)


# 打印 10
demo2()
# 打印 2
print(x)
```

### class

```python
class People:
    # 类比构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 私有属性,只能在类中修改
        self.__var = 10
        self.__birthday = 20

    # 对象方法
    def sayhi(self):
        print("Hi,my name is {}, age is {}".format(
            self.name, self.age
        ))

    def getvar(self):
        return self.__var

    # 控制修改属性调用方法
    @property
    def birthday(self):
        return self.__birthday

    # 修改私有变量,通过 someone.birthday= 20 ,通过这种方式就可以对参数进行校验
    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday


someone = People('zhangSan', 21)
someone.sayhi()
someone.age = 22
#
People.__var = 20
print(someone.getvar())
# 20
print(someone.birthday)
someone.birthday = 30
# 30
print(someone.birthday)

```

### import

```python
import sys

# 从当前目录和 sys.path 导包
from package.demo.fileutil import test

print(sys.path)

test()
```

### io

```python
f = open('../../a.txt')
print(f.read())
f.close()
```

### 包安装

```shell
pip3 install requests
```

### 爬虫