import concurrent.futures
import time
import multiprocessing
from concurrent.futures import as_completed

count = multiprocessing.cpu_count()
print(f"cpu 核心数：{count}")


# 定义一个任务函数
def task(num: int):
    print(f"Task {num} is executing...")
    time.sleep(num)
    if num == 8:
        raise Exception('抛异常')
    print(f"Task {num} is after...")
    return f"Task {num} is done."


def main():
    # 创建一个ThreadPoolExecutor对象，指定最大线程数为3
    futures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
        print("第 1 个")
        futures.append(executor.submit(task, 6))
        print("第 2 个")
        futures.append(executor.submit(task, 5))
        print("第 3 个")
        futures.append(executor.submit(task, 8))
        print("第 4 个")
        futures.append(executor.submit(task, 80))
        for f in as_completed(futures):
            exception = f.exception()
            if exception:
                raise exception
            else:
                print(f.result())


if __name__ == "__main__":
    main()
