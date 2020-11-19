# 循环，使用 while 编写循环语句，和 C 相同

number = 1
while number <= 100:
    print(number, end=' ')
    number += 1
print('')

# for 语句的使用: 可以用于遍历所有的可迭代类型，每次循环从序列中获取第(循环次数)个的元素，
# 将元素赋值给 for 和 in 中间所提供的变量中，可以被直接的访问到
for letter in 'hello 15pb':
    print(letter)

# 使用 range 可以快速生成一个指定规则的列表，参数同切片
print(list(range(1, 100, 3)))

# 通过 range 生成一个可迭代序列，从中取出元素，并输出
for value in range(101):
    print(value)


# while 一般用于不确定的循环，for 一般用于序列的遍历
# break 和 continue 和 C++ 的完全一致，对于break，for 和 while 有扩展语法

for i in range(100):
    # 对于 for else 或者 while else 语句，如果采用 break 跳出
    # 循环就不执行 else，如果正常退出则执行
    pass
else:
    print('正常退出')