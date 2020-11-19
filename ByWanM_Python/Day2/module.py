print('我是一个模块 1')
print('我是一个模块 2')

module_value1 = 1
module_value2 = 1
module_value3 = 1

# 通过在模块内的变量前添加单下划线，可以设置变量为模块私有的
# 私有意味着，不能通过 from m import * 的方式访问
_module_private_value = 1000

# 通常模块内的所有代码都会在被导入时直接的运行，但是有些时候
# 模块内的代码被用于进行单元测试(测试模块内函数的可行性)
if __name__ == "__main__":
    # 如果当前模块是直接运行的模块就是主模块
    print(__name__)

# 这一条语句无论如何都被运行
print(__name__)