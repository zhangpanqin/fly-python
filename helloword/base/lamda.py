import logging

logging.basicConfig(level='INFO',filename='test.log')
a = [1, 2, 3, 4]
if __name__ == '__main__':
    for it in map(lambda x: x + 2, a):
        logging.info("测试")
        print(it)
