# 创建一个父类，提供了自己的属性和方法
class Parent(object):
    # 父类提供的类属性
    parent_value = 1000

    # 构造方法，父类的构造方法
    def __init__(self, name):
        print(f'Parent.__init__({name})')


class Parent2(object):
    parent_value = 2000

    def __init__(self):
        print(f'Parent2.__init__()')


# 创建一个子类，继承自 Parent
class Child(Parent, Parent2):

    # 如果子类没有提供构造方法，就会使用父类的构造方法
    def __init__(self):
        print('Child.__init__()')
        # 不会自动调用父类的构造方法
        Parent.__init__(self, 'xiaoming')
        # 使用 super 调用父类的构造方法
        super().__init__('xiaoming')

        # 如果对 super 进行传参，那么实际调用的将是参数
        # 一在 mro(继承) 链中的下一个类的方法
        Parent2.__init__(self)
        super(Parent, self).__init__()
        super(Child, self).__init__('xiaoming')


    # 在子类中访问父类是属性
    def visit_value(self):
        # 直接以类名进行访问，访问父类的属性
        print(Parent.parent_value)

child = Child()
child.visit_value()
print(Child.__mro__)


#                          object(1)
#               parent1(3)         parent2(2)
#                child(parent1, parent2)(4)


# python 中继承的核心就是 mro