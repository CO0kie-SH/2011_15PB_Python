# 在 python 中，变量不需要被事先创建，第一次出现赋值语句时会自动创建
value = 100

# python 中的变量类似于一个void*指针，可以指向任何的类型，使用id看地址
print(hex(id(value)))

# python 是一个动态类型的语言，变量的类型在运行过程中会由于赋值的类型
# 不同动态的改变。python 在使用非数值类型赋值时，实际上创建了一块内存
# 空间用于保存该类型对应的数据，并设置其引用计数，当引用计数为 0 时，
# 该对象会被自动的销毁
content = '15pb'
import sys
print(sys.getrefcount('15pb'))
del content
print(sys.getrefcount('15pb'))