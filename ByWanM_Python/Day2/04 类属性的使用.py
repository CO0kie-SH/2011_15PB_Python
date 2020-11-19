# 定义一个类，类内添加了类属性
class Demo(object):
    # 一个类属性
    class_value = 0


demo = Demo()
# 想要访问类属性，可以使用类名以及实例名(不推荐)
print(demo.class_value)
print(Demo.class_value)

# 对于类属性的修改，
demo.class_value = 100          # 创建了一个同名的实例属性
print(Demo.class_value)
Demo.class_value = 200          # 修改类属性只能使用类名
print(Demo.class_value)

# 动态增减类属性的方式
#   增加: 通过类名或类方法中的 cls 关键字可以动态添加
Demo.class_value2 = 1000
print(Demo.__dict__)        # 包含类内所有的属性组合的键值对
#   删除: 通过关键字 del 进行删除
del Demo.class_value
print(Demo.__dict__)