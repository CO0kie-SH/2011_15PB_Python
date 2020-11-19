# 一个类，包含了实例属性的使用
class Demo(object):

    # 如果在构造方法内添加实例属性，可以保证每一个实例都拥有
    def __init__(self, value):
        self.value = value

    # 一个实例方法，其中使用了 self 关键字添加实例属性
    def add_value(self):
        self.value1 = 0


# 创建一个实例(每个实例都有自己的属性)
demo1 = Demo(1000)
demo2 = Demo(2000)

# 输出两个实例中的所有元素
print(demo1.__dict__)
print(demo2.__dict__)

# 通过 self 以及实例名动态的添加属性
demo1.add_value()
demo2.value2 = 1000
print(demo1.__dict__)
print(demo2.__dict__)
