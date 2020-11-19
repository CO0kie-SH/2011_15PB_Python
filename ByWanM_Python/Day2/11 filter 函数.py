# filer: 将参数二指定的序列中，每一个元素都传入到参数一指定的函数中
#   如果该函数返回为 true，就将元素保存到一个新的序列中，否则丢弃

# 该函数最少需要有一个参数，用于接收序列中的每一个元素
def filer_function(letter):
    # 如果是大写的，就保留，否则丢弃
    return letter.isupper()


def filer_function2(value):
    return True if value % 3 == 0 else False


print(list(filter(filer_function, 'AaBbCcDdEeFfGg')))
print(list(filter(filer_function2, range(1000))))