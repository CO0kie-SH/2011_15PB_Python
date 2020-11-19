class Demo(object):
    # 仅双下划线开头表示这是私有的
    __private_value = 1000

    # __slots__ 可以限定我们能够创建什么样的属性
    __slots__ = ('value1', 'value2')

    # 通常双下划线开头表示私有，双下划线开头结尾表示解释器提供
    # 单下划线开头约定俗称是私有的，但实际没有任何控制

# 通过 __dict__ 属性查看当前类内的所有类属性
print(Demo.__dict__)

# python 中的私有实际只是以一定的方式为属性修改了名称: _类名+属性名
print(Demo._Demo__private_value)

# 创建实例并使用实例动态添加属性
demo = Demo()
demo.value1 = 1000
demo.value2 = 1000
demo.value3 = 1000


class Demo2(object):
    def __init__(self, name: int, age: int):
        self._name = name
        self._age = age

# 类魔术方法的重定义: __add__ __truediv__ __init__ __str__