# map: 可以传入多个序列，参数一要求传入一个函数，函数接收的参数
#   个数必须和传入的序列个数相同，在使用 map 的时候，会分别将每
#   一个序列中的每一个元素传入函数，并且将函数的返回值组合成新
#   的序列

def function(left, right):
    return left* right

print(list(map(function, 'abcdefg', [1, 2, 3, 4, 5, 6, 7])))
