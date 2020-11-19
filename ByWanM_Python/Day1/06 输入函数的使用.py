# 通过 input 可以直接完成一个交互式的输入
value = input('请输入一个整数: ')

# 输入的任何数据最终都会是一个字符串
print(value, type(value))

# 通过强制类型转换或 eval 函数可以转换类型
value = int(input('请输入第二个数: '))
print(value, type(value))
