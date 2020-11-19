# 使用 threading 可以实现线程操作(伪线程)
import threading
import time


# 定义一个全局的锁
lock = threading.Lock()


# 不带参数的线程回调函数
def worker_thread():
    for i in range(1000):
        lock.acquire()
        # current_thread 表示的始终都是当前的线程
        print(threading.current_thread().name, i)
        time.sleep(0.1)
        lock.release()


# 模拟主函数的使用
def main():
    # 通过 Thread 函数创建一个线程，需要指定起始位置(函数)
    t = threading.Thread(target=worker_thread, name='worker_thread')
    # Thread 创建的实际是线程对象，默认并没有运行，需要调用 start 函数
    t.start()

    for i in range(1000):
        lock.acquire()
        # current_thread 表示的始终都是当前的线程
        print(threading.current_thread().name, i)
        time.sleep(0.1)
        lock.release()

    # 通常，为了确保主线程退出之前，所有其它线程执行完毕，需要等待
    t.join()


if __name__ == '__main__':
    main()




