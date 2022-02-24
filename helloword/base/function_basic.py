def demo(a, b='默认'):
    print('a=', a)
    print('b=', b)


demo('11', 'a')
demo(b='a', a='11')

x = 2


def demo2():
    x = 10
    print(x)


demo2()
print(x)


def demo3(*args):
    print(type(args))


demo3('a')


def demo4(**kwargs):
    print(type(kwargs))
    print(kwargs)


demo4(a=1, b=2)
