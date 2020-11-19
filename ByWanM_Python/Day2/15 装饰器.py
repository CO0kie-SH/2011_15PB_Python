# python 中高阶函数的定义: 参数或返回值为函数的函数就是高阶函数

# 闭包: 内部函数使用了外部函数的局部变量
def outer(left):
    def inner(right):
        return left * right
    return inner


# 将做操作数传入给函数，实际上返回的是下列函数
"""
    def inner(right):
        return 10 * right 
"""
inner = outer(10)

# 可以调用返回的函数，传入右操作数并得到结果
print(inner(20))


# 装饰器: 在闭包的基础上，使用了外部传入的函数
#   作用: 在不更改函数名称，参数个数和调用方式的前提下为某个函数添加新的功能

def w1(func):
    def inner():
        print('这里是新添加的内容')
        func()
        print('这里也是新添加的内容')
    return inner

# @w1
# f1 是需要被装饰的函数
def f1():
    print('f1')

f1()


# 装饰器实际上叫做语法糖，例如数组 arr[i][j] -> *(*(arr+i)+j)
"""
    def 新的f1():
        print('这里是新添加的内容')
        f1() -> 旧的
        print('这里也是新添加的内容')
"""
f1 = w1(f1)         # @w1  def f1(): ....
f1()
