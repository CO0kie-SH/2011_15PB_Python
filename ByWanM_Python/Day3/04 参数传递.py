import threading


# 线程回调函数，带参
def thread1(arg1, arg2, arg3):
    print(arg1, type(arg1))
    print(arg2, type(arg2))
    print(arg3, type(arg3))


# 线程回调函数，带元组变参
def thread2(*args):
    print(args, type(args))


# 线程回调函数，带字典变参
def thread3(**kwargs):
    print(kwargs, type(kwargs))


# 线程回调函数，带元组和字典变参
def thread4(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))


# 创建多个线程，传递相应的参数
threading.Thread(target=thread2, args=(1, 2, 3)).start()
threading.Thread(target=thread3, kwargs={"a": 1, "b": 2, "c": 3}).start()
threading.Thread(target=thread4, args=(1, 2, 3), kwargs={"a": 1, "b": 2, "c": 3}).start()
threading.Thread(target=thread1, args=(1, 2, 3)).start()