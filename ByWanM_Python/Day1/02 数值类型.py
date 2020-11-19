# python 中的基本类型: int(无限长度)，float(小数)
print(1024, type(1024))
print(3.14, 314e-2, type(3.14))

# 整数类型不同形式的表现(输出)
print(hex(100), bin(100), oct(100))

# 整数类型不同形式的表现(输入)
print(0b1100100, 0x64, 0o144)

# 将字符串转换成整数类型
print(int('1000'), type(int('1000')))
print(int('1000', 16), int('1000', 8))
