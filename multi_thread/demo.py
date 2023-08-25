import threading
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))


if __name__ == '__main__':
    t1 = threading.Thread(target=print_time, args=("1", 2), name="Thread-1")
    t2 = threading.Thread(target=print_time, args=("2", 3), name="Thread-2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
