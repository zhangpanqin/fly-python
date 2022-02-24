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

### 包安装

```shell
pip3 install requests
```

### 爬虫