try:
    # 包含的是可能产生异常的语句
    print(10 / 1)
except ZeroDivisionError:
    # 如果产生了异常，就跳转到这个位置执行
    print('产生了异常')
else:
    # 正常情况下，所执行的代码
    print('没有产生异常')


# 如果接收的异常类型和实际产生的不一致，就接收不了异常
try:
    print(10 / 0)
except ZeroDivisionError: #NameError:
    print('产生了名称异常')


# 在 python 中，产生任何一个异常都会抛出一个异常对象，
# 通过 except type as name 的方式可以接收到异常对象
try:
    l = []
    print(l[0])
    # 接收到了 IndexError 异常对象并取名为 e
except IndexError as e:
    print(e)


# 通常为了节省时间和精力会直接使用精简写法
try:
    pass
# Exception 是通用异常(语法\网络\文件)的基类，通过这个类型
# 就可以接收到大多数的异常了
except Exception as e:
    pass


import sys


# 通过 finally 可以保证程序无论以何种方式正常退出，其中的代码都被执行
#   例如这些语句: return continue break sys.exit(0)
try:
    if True:
        # sys.exit(0)
        pass
finally:
    # 用于执行清理操作
    print('finally')


# 主动抛出异常，如果想要自定义异常，可以实现一个自己的继承自 BaseException 的异常类
# 然后通过 raise 主动的抛出这个类型，并进行处理
password = input('password: ')
if len(password) < 8:
    raise Exception('密码长度过短')