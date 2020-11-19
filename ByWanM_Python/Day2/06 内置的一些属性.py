# 定义一个空类，用于测试内部属性
class Demo(object):
    pass

# 如果想看到一个类提供了哪些属性，就使用 dir
print(dir(Demo))

# 可以使用 help 查找某一个类的帮助信息
print(help(list))

# 可以通过内置的一些属性，输出想要的内容
print(Demo.__dict__)