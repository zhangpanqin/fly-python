import concurrent.futures
import time
import multiprocessing

count = multiprocessing.cpu_count()
print(f"cpu 核心数：{count}")


# 定义一个任务函数
def task(num):
    print(f"Task {num} is executing...")
    time.sleep(10)
    return f"Task {num} is done."

def main():
    # 创建一个ThreadPoolExecutor对象，指定最大线程数为3
    with concurrent.futures.ThreadPoolExecutor(max_workers=count) as executor:
        # 提交任务给线程池，并返回Future对象列表
        futures = [executor.submit(task, i) for i in range(10)]

        # # 遍历Future对象列表，获取任务的结果
        for future in concurrent.futures.as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    start_time = time.time()
    main()
    # 记录结束时间
    end_time = time.time()

    # 计算时间间隔
    elapsed_time = end_time - start_time

    print("代码片段执行时间为:", elapsed_time, "秒")

