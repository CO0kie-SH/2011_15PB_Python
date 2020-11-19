# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201110 -*-


def list1():
	global gList
	lst2 = list(set(gList))
	lst2.sort(key=gList.index)
	return lst2


def list2():
	global gList
	data = gList.copy()
	return sorted(set(data), key=data.index)


gList = [11, 2, 3, 4, 4, 2, 6, 3, 3, 2]


# n的阶乘和
def t8_4_1(num: int):
	imax = 0
	for i in range(1, num + 1):
		sum2 = 1
		for j in range(1, i + 1):
			sum2 *= j
		imax += sum2
	return imax


# 水仙花
def t8_4_2(num: int):
	lv = []
	for i in range(100, num, 1):
		num_sum = 0
		for x in str(i):
			num_sum += int(x) ** 3
		if i == num_sum:
			lv.append(i)
	return lv


# 圣诞树
def t8_4_3(line: int):
	for i in range(1, line + 1):
		print(' ' * (line - i), i * '*', (i - 1) * '*', sep='')
	return '-' * 7


# 实心菱形
def t8_4_4(line: int):
	for i in range(1, line):
		print(' ' * (line - i), i * '*', (i - 1) * '*', sep='')
	for i in range(line, 0, -1):
		print(' ' * (line - i), i * '*', (i - 1) * '*', sep='')
	return '-' * 7


# 空心菱形
def t8_4_5(line: int):
	for i in range(0, line):
		print(' ' * (line - i - 1), end='*')
		print(' ' * (2 * i - 1), end='')
		print('*' if i > 0 else '')
	for i in range(1, line):
		print(' ' * i, end='*')
		print(' ' * ((line - i) * 2 - 3), end='')
		print('*' if i < line - 1 else '')
	return '-' * 7


# 杨辉三角
def t8_4_7(line: int):
	if line < 0 or line > 999:
		return
	g = [1]
	for n in range(line):
		print(g)
		g.append(0)
		g = [g[i] + g[i - 1] for i in range(len(g))]
	return '↑↑↑\tt8.4.7_杨辉三角'


# 杨辉三角生成器
def t8_4_7_ex(line: int):
	if line < 0 or line > 999:
		return
	g = [1]
	for n in range(line):
		yield g
		g.append(0)
		g = [g[i] + g[i - 1] for i in range(len(g))]
	return '↑↑↑\tt8.4.7_杨辉三角生成器'


# 冒泡排序
def t8_4_6():
	ls = [20, 30, 40, 3, 6, 47, 25, 77, 15]
	for i in range(len(ls)):
		for j in range(1 + i, len(ls)):
			if ls[i] > ls[j]:
				ls[i], ls[j] = ls[j], ls[i]
	return ls


# 斐波那契普通版
def f01_fib(line: int):
	print('-' * 9, '斐波那契')
	n, a, b = 0, 0, 1
	while n < line:
		print(b, end=' ')
		a, b = b, a + b
		n = n + 1
	return '-' * 9 + '<斐波那契'


# 斐波那契生成器
def f01_fib2(line: int):
	print('-' * 9, '斐波那契')
	n, a, b = 0, 0, 1
	while n < line:
		yield b
		a, b = b, a + b
		n = n + 1
	return '-' * 9 + '<斐波那契'


# 斐波那契生成器
def f01_fib3(line: int):
	print('-' * 9, '斐波那契')
	n, a, b = 0, 0, 1
	lv = []
	while n < line:
		lv.append(b)
		a, b = b, a + b
		n += 1
	return lv


# map使用
def t18_1_1_map():
	pass


if __name__ == '__main__':
	print(list1())
	print(list2())
	print(t8_4_1(5))
	print(t8_4_2(1000))
	print(t8_4_3(4))
	print(t8_4_4(4))
	print(t8_4_5(4))
	print(t8_4_7(9))
	print(t8_4_6())
	print(f01_fib(9))
	for x in f01_fib2(9):
		print(x, end=' ')
	print(tuple(f01_fib2(9)), '-' * 9, '斐波那契2')
	print('斐波那契3', f01_fib3(100)[-1:])
	for x in t8_4_7_ex(10):
		print(x)
	t18_1_1_map()
	pass

# <editor-fold desc="进制转换">
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

# 将字符串转小数
print(round(3.1415, 3))  # 四舍五入 进位
print(round(3.45, 1))  # 四舍五入 进位
print(round(3.35, 1))  # 四舍五入 没有进位
print(round(3.5))  # 四舍五入 进位
print(round(2.5))  # 四舍五入 没有进位
# 只有当n+1位数字是5的时候，容易混淆，
# 如果n为偶数，则n+1位数是5，则进位，
# 例如round（1.23456，3）最终变为1.235
# 如果n为奇数，则n+1位是数5，那不进位，
# 例如round（2.355，2），最终为2.35
# 如果n为0，即没有填写n的时候，最终结果与上面相反，
# 即整数部分为偶数的时候，小数位5不进位，例如（round（2.5）变为2）。
str_s = '3.1415926'
flo_s = float(str_s)
print(flo_s, type(flo_s))
print('%.3f%%' % flo_s)
print(f'{flo_s:.3f}%')
# 方法三：Decimal（）函数
from decimal import Decimal

flo_f = Decimal(flo_s).quantize(Decimal('0.000'))
print(flo_f, str(flo_f) + '%')
# </editor-fold>


lv = list(i + 1 for i in range(10))
print(lv[-5:])  # [后5个数]
print(lv[-5:7])  # [后5个数起,到第7个数]
print(lv[-5:-1])  # [后5个数起,到倒数第一个)  左开右闭
