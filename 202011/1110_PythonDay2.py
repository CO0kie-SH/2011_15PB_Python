# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201111 -*-


# <editor-fold desc="类的限制">
class Demo(object):
	# 仅双下划线开头表示这是私有的
	__private_value = 1000
	# __slots__ 可以限定我们能够创建什么样的属性
	__slots__ = ('value1', 'value2')


# 通过 __dict__ 属性查看当前类内的所有类属性
print(Demo.__dict__)
# python 中的私有实际只是以一定的方式为属性修改了名称: _类名+属性名
print(Demo._Demo__private_value)
# 创建实例并使用实例动态添加属性
demo = Demo()
demo.value1 = 1000
demo.value2 = 1000


# demo.value3 = 1000    #会报错
# </editor-fold>

# <editor-fold desc="类的继承">
# 创建一个父类，提供了自己的属性和方法
class Parent(object):
	# 父类提供的类属性
	parent_value = 1000

	# 构造方法，父类的构造方法
	def __init__(self, name):
		print(f'Parent.__init__({name})')


class Parent2(object):
	parent_value = 2000

	def __init__(self):
		print(f'Parent2.__init__()')


# 创建一个子类，继承自 Parent
class Child(Parent, Parent2):

	# 如果子类没有提供构造方法，就会使用父类的构造方法
	def __init__(self):
		print('Child.__init__()')
		# 不会自动调用父类的构造方法
		Parent.__init__(self, 'xiaoming')
		# 使用 super 调用父类的构造方法
		super().__init__('xiaoming')

		# 如果对 super 进行传参，那么实际调用的将是参数
		# 一在 mro(继承) 链中的下一个类的方法
		Parent2.__init__(self)
		super(Parent, self).__init__()
		super(Child, self).__init__('xiaoming')

	# 在子类中访问父类是属性
	def visit_value(self):
		# 直接以类名进行访问，访问父类的属性
		print(Parent.parent_value)


child = Child()
child.visit_value()
''' obj
Par1    Par2
	child
'''
print(Child.__mro__)  # 4231


# </editor-fold>

# 高级函数-过滤函数
# <editor-fold desc="filter函数">
def filer_function(letter):
	# 如果是大写的，就保留，否则丢弃
	return letter.isupper()


def filer_function2(value):
	return True if value % 3 == 0 else False


print(list(filter(filer_function, 'AaBbCcDdEeFfGg')))
print(list(filter(filer_function2, range(1000))))
# </editor-fold>

# <editor-fold desc="reduce函数">
import functools


# reduce: 第一个参数是一个函数，该函数一定要接收两个参数，在使用
#   reduce 时，第一次会将可迭代对象红的元素一和元素二传入到函数中，
#   计算出一个返回值，接下来每次都将函数的返回结果和下一个元素进行
#   计算，知道序列遍历结束
def add_value(left, right):
	return left + right


def mul_value(left, right):
	return left * right


# 首先将 1 和 2 放入函数，返回 3，再将 3 和 3 计算返回 6，再将 6 和 4
# 计算返回 10，最终一直加到 10，返回的是 10 到 1 相加的和
print(functools.reduce(add_value, range(1, 11)))
print(functools.reduce(mul_value, range(1, 11)))

from functools import reduce


def fn(x, y):
	return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


# </editor-fold>

# <editor-fold desc="map函数">
# map: 可以传入多个序列，参数一要求传入一个函数，函数接收的参数
#   个数必须和传入的序列个数相同，在使用 map 的时候，会分别将每
#   一个序列中的每一个元素传入函数，并且将函数的返回值组合成新
#   的序列

def function(left, right):
	return left * right


print(list(map(function, 'abcdefg', [1, 2, 3, 4, 5, 6, 7])))


def f(x):
	return str(x)


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# </editor-fold>

# sorted成绩排序
# <editor-fold desc="sorted函数">
from operator import itemgetter

L = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))
print(sorted(L, key=str.lower))

students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))
# </editor-fold>

# lambda 表达式的语法，表达式的结果是一个匿名函数
# <editor-fold desc="lambda 表达式">
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


# </editor-fold>

# <editor-fold desc="装饰器">
# python 中高阶函数的定义: 参数或返回值为函数的函数就是高阶函数

# 闭包: 内部函数使用了外部函数的局部变量
def outer(left):
	def inner(right):
		return left * right

	return inner


# 将做操作数传入给函数，实际上返回的是下列函数
"""
    def inner(right):
        return 10 * right 
"""
inner = outer(10)

# 可以调用返回的函数，传入右操作数并得到结果
print(inner(20))
print(outer(20)(10))


# 装饰器: 在闭包的基础上，使用了外部传入的函数
#   作用: 在不更改函数名称，参数个数和调用方式的前提下为某个函数添加新的功能

def w1(func):
	def inner():
		print('这里是新添加的内容')
		func()
		print('这里也是新添加的内容')

	return inner


# @w1
# f1 是需要被装饰的函数
def f1():
	print('f1')


f1()

# 装饰器实际上叫做语法糖，例如数组 arr[i][j] -> *(*(arr+i)+j)
"""
    def 新的f1():
        print('这里是新添加的内容')
        f1() -> 旧的
        print('这里也是新添加的内容')
"""
f1 = w1(f1)  # @w1  def f1(): ....
f1()
# </editor-fold>

# <editor-fold desc="time模块">
print('\n', '↓' * 9, 'time模块')
import time

# 获取当前的时间戳(使用浮点数记录的秒数)
print(time.time())

# 将指定的时间戳转换为当前时区的元组
print(time.localtime())
print(time.gmtime())  # 标准时区

# 将时间元组转换为时间戳
print(time.mktime(time.localtime()))

# 睡眠一定的时间
time.sleep(0.100)

# 将时间元组转换成时间字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# </editor-fold>

# <editor-fold desc="random模块">
print('\n', '↓' * 9, 'random模块')
import random

# randint 和 randrange
for i in range(10):
	# 生成 0<=value<=10 的一个随机数值
	print(random.randint(0, 10), end=' ')
	# 先生成一个 range 序列，从中获取一个随机值
	print(random.randrange(0, 10), end='|')
print()

# 创建一个字符串，用于保存验证码
tmp = ""
# 主要在于遍历的次数，循环 6 次
for i in range(6):
	# 生成一个满足 range 条件的随机值
	rad1 = random.randrange(4)
	# 有一半的概率进入下面的两个分支
	if rad1 == 1 or rad1 == 3:
		# 生成一个随机的整数并转换为字符串添加到末尾
		rad2 = random.randrange(0, 10)
		tmp += str(rad2)
	else:
		# 生成一个随机的大小字母添加到结尾
		rad3 = random.randrange(65, 91)
		tmp += chr(rad3)
print(tmp)

# 从指定序列中随机取出一个元素
print(random.choice(['饭', '粥', '面', '饿']))

# 打乱一个序列(洗牌)
l = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(l)
print(l)
# </editor-fold>

# <editor-fold desc="os目录管理">
# os 模块提供了目录和文件能够执行的一些操作
import os

base = r'D:\Videos\\'

# 通过循环获取到指定目录下的所有文件和文件夹
for name in os.listdir(base):
	# 判断目标名称是否为文件
	if os.path.isfile(base + name):
		# 输出文件名称以及后缀名
		print(os.path.splitext(name))
# </editor-fold>

# <editor-fold desc="hashlib模块">
print('\n', '↓' * 9, 'hashlib模块')
import hashlib

m = hashlib.md5()
m.update(b'ABC')
print(m.hexdigest())
print(hashlib.md5(b'ABC').hexdigest())

import base64

url = "https://www.cnblogs.com/songzhixue/"
bytes_url = url.encode("utf-8")
str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
print(1, str_url)
str_url = base64.b64decode(str_url).decode('UTF-8')
print(2, str_url)

# </editor-fold>

# 首字母
lv = ['adam', 'LISA', 'barT']
lv = list(map(lambda x: x.title(), lv))
print(lv)

# 计算乘积
lv = [3, 5, 7, 9]
sum = functools.reduce(lambda x, y: x * y, lv)
print(sum)


# 字符串转小数
def str2float(s):
	sum1, sum2 = 1, 0
	str_s = s.split('.')
	for s in str_s[1]:
		sum2 = sum2 * 10 + int(s)
		sum1 *= 10
	sum2, sum1 = sum2 / sum1, 0
	for s in str_s[0]:
		sum1 = sum1 * 10 + int(s)
	return sum1 + sum2


def str2float2(s):
	num1, num2 = s.split('.')
	return int(num1) + int(num2) / 10 ** len(num2)


def str2float3(s):
	lv = list(filter(lambda ch: ch.isdigit(), s))
	sum = functools.reduce(lambda x, y: int(x) * 10 + int(y), lv)
	return sum / 10 ** (len(s) - s.find('.') - 1)


print('str2float(\'123.456\') =', str2float('1230.4560'))
print('str2float2 =', str2float2('100.0405600000'))
print('str2float3 =', str2float3('100.0405600000'))

if __name__ == '__main__':
	pass
