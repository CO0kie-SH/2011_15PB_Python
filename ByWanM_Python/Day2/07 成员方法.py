# 在类内测试python提供的三种成员方法
class Demo(object):

    # 实例方法: 第一个参数表示的是调用当前方法的实例，类似 this，通常名称为
    #   self，也可以换做其它名称(不推荐)，通过 self 可以动态操作实例属性
    def member_function(self):
        print('member_function')

    # 类方法: 第一个参数表示当前方法所在的类，类似类名，通常名称为 cls，类
    #   方法常用于需要访问类属性但是不访问实例属性的情况
    @classmethod
    def class_function(cls):
        print('class_function')

    # 静态方法: 对方法名没有任何的要求，如果方法没有访问任何的属性，就可以设为静态的
    @staticmethod
    def static_method():
        print('static_method')