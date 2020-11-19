# class 开头后面紧跟类名，类名的首字母应该大写，后面的括号中是父类
# python3 定义的类称之为新式类，无论是否显式说明父类的 object，默
# 认都继承自 object，并且继承下来了一些内置的方法
class Student(object):
    # 类内直接定义了一些变量，被称为[类]属性，所有的类属性
    # 归类所有，能够被任何一个实例访问到，类似于静态变量
    count = 0
    books = []

    # 构造访问，任何一个类都拥有名称为 __init__ 的构造方法，
    # 当一个实例被创建之后，会被自动的调用
    def __init__(self, name, age):
        # 所有使用 self 以及实例名创建的变量都成为实例属性
        # 每一个实例都拥有自己的实例属性，可以动态添加
        self.name = name
        self.age = age
        print('这是一个构造方法')

    # 任何一个类都拥有名称为 __del__ 的析构方法
    def __del__(self):
        print('这是一个析构方法')


# 如果存在构造方法，那么创建实例的时候，必须提供除
# self 以外的其它所有参数，self 类似于 this，表示
# 调用方法的是哪一个实例
objStudent1 = Student("xiaoming", 19)
