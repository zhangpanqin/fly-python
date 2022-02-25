import sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(abspath(dirname(__file__)), '../')))
# 当前目录和系统目录导包
from package.demo.fileutil import test

if __name__ == '__main__':
    print(sys.path)
    test()
