# 算数运算符: 幂运算 **
print(2 ** 1024)

# 算数运算符: 除法运算 /(真除法) //(向下取整除法)
print(10 / 10, 10.0 / 3)
print(10 // 3, -10.0 // 3)

# 比较运算 == 和身份运算符 is
l1 = [1, 2, 3]
l2 = l1
print(hex(id(l1)), hex(id(l2)), l1 == l2, l1 is l2)
l2 = l1.copy()
print(hex(id(l1)), hex(id(l2)), l1 == l2, l1 is l2)

# 成员关系运算符: 判断某元素是否在某容器中
print('a' in 'abc', 'd' in 'abc')

