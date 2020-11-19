# 判断用户输入的用户名和密码是否符合长度且匹配

# 接收用户的输入
username = input('username: ')
password = input('password: ')

# 判断用户输入的长度是否准确
if len(username) >= 8 and len(password) >= 8:
    # if 后面直接添加表达式，结尾必须添加冒号(:)
    if username == 'username' and password == 'password':
        # if 后面的语句必须拥有一级缩进，并且所有存在一级缩进
        # 的语句都被认为是语句块的一部分，累哦四花括号作用域
        print('登录成功，跳转至个人中心...')
        print('这里是第二条语句，同样是输出的')
else:
    print('用户名或密码的长度不够')


# 多分枝结构，通过 if ... elif ... else ... 来实现，使用方法同 C