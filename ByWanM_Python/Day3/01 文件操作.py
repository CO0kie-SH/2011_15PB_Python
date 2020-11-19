# 使用 Python 内置函数完成文件操作

# 参数一是文件所在的路径，参数二是打开方式，可能需要注意 encoding
file = open('content.txt', 'w+')

# 向文件的内部写入数据
file.write('hello 15pb')
file.writelines(['第一行\n', '第二行\n', '第三行\n'])

# 关闭文件，将对文件的修改保存到硬盘
file.close()

# 通过 with open() as name 的形式打开一个文件
with open('content.txt', 'r') as file:
    # 将 open 函数的返回值保存到变量 file 中
    # 对于文件对象，在离开 with 作用域的时候
    # 会自动的进行关闭，只需要关注逻辑部分
    print(file.read())          # 默认读取所有内容
    print(file.readline())      # 一行最大字符个数
    print(file.readlines())     # 读取的最多行数

# 以只读方式打开文件的时候，如果文件不存在就会产生异常
try:
    with open('content2.txt') as file:
        pass
except Exception as e:
    print(e)

# 更多的函数: file.seek + file.tell -> 计算文件大小

# 文件操作模块: os，os 的使用方式和 C 语言的函数完全一致