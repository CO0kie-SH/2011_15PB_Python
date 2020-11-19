# 全局变量: 定义在所有函数之外的变量
g_number = 0


# 局部变量: 定义在任何一个函数之内的变量
def function1():
    l_number = 1
    # 分别用于输出当前的全局变量以及所在作用域的局部变量
    print(globals(), locals())


function1()


# 尝试在函数中访问一个全局变量
def function2():
    # 在局部空间中可以直接访问全局变量
    print(g_number)


function2()


def function3():
    # 一旦尝试在函数内修改全局变量，实际上会定义出一个
    # 和全局变量同名的局部变量
    g_number = 10000
    print(locals(), globals())


function3()


def function4():
    # 通过 global 关键字，可以声明使用的是全局范围内的 g_number
    global g_number
    g_number = 100000000
    print(locals(), globals())


function4()


def function5():
    # 如果想在函数内定义一个全局变量，也可以使用 global
    global g_value2
    g_value2 = 0x12345
    print(locals(), globals())


function5()
