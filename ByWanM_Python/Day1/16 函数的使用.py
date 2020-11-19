# 函数定义的简单例子
def my_max(value1=0, value2=0):
    # 类似三目运算符的写法
    return value1 if value1 > value2 else value2


# 新的写法，可以限制传入的类型
def my_min(value1: int, value2: int) -> int:
    return value1 if value1 > value2 else value2


# pass 类似于 C 语言中的单个分号，即什么也不做，如果一个
# 函数没有显示的指定返回值，那么就返回 None
def no_return():
    pass


print(no_return())


# 参数的传递: 位置传参，按照定义顺序传参
print(my_min(10, 20))

# 参数的传递: 关键字传参，按照形参名传参(很常见)
print(my_min(value2=10, value1=20))


# 变参的传递: 传元组 *args
def args_function(*args):
    print(args, type(args))


args_function(1, 2)
args_function(1, 2, 3)


# 变参的传递: 传字典
def kwargs_function(**kwargs):
    print(kwargs, type(kwargs))


kwargs_function(a=1, b=2, c=3)
kwargs_function(a=1, b=2, c=3, d=4)


# 两种方式一般组合使用，在使用的时候，要求字典必须在后面
def all_fucntion(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
