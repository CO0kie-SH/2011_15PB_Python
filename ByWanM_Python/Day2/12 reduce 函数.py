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

