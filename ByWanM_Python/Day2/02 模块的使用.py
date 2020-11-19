# 任何一个以 .py 结尾的文件，都被成为模块，可以使用 import 语句导入
# 导入的时候首先需要找到目标模块，接下来将目标模块转换成字节码，使用
# PVM执行字节码，由于这是一个十分消耗性能的事情，所以 python 只允许
# 我们对一个模块直接进行一次导入
import module
import module

# 如果一定想要代码被执行多遍，可以使用内置模块 importlib
import importlib
importlib.reload(module)

# 如何使用模块中的内容（概念类似C++中的头文件和命名空间）
import module                       # 类似于 #include <iostream>
print(module.module_value1)

from module import module_value2    # 类似于在包含头文件的基础上 using std::name
print(module_value2)

from module import *                # 在包含头文件的基础上 using namespace std
print(module_value3)

# 单下划线开头的模块全局变量只能使用命名空间访问
print(module._module_private_value)