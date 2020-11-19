# lambda 表达式的语法，表达式的结果是一个匿名函数
func = lambda letter, count: letter * count

# 1. 参数使用逗号隔开
# 2. 函数体使用冒号隔开
# 3. 函数体只能有一条语句
# 4. 函数体内的一条语句会被作为返回值
print(func('a', 10))


import functools


# 使用匿名函数可以在某些程度上，减少代码量
print(list(filter(lambda letter: letter.isupper(), "AaBbCcDdEeFfGg")))
print(functools.reduce(lambda left, right: left * right, range(1, 11)))
print(functools.reduce(lambda left, right: left + right, range(1, 11)))
print(list(map(lambda letter, count: letter * count, "abcdefg", [1, 2, 3, 4, 5, 6, 7])))
