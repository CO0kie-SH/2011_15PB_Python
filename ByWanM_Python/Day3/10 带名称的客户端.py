from socket import *
from struct import *
from threading import *


# 线程回调函数: 接收来自另一边的信息
def reciver(sock):
    while True:
        try:
            # 如果客户端或服务器断开连接，会产生异常
            print(sock.recv(100).decode('utf-8'))
        except Exception as e:
            print('error', e)
            # 一定要记得 break 跳出当前的循环
            break


def main():
    # 1. 创建套接字对象
    client = socket(AF_INET, SOCK_STREAM)

    # 2. 等待客户端的连接
    client.connect(('127.0.0.1', 0x1515))

    # 填写用户名和密码尝试进行登录
    username = input('username: ')
    password = input('password: ')
    content = pack('32s32s', username.encode(), password.encode())
    client.send(content)

    # 接收登录的结果，如果失败，就退出
    if client.recv(100).decode() == '不ok':
        return
    print('xxxxxxx')

    # 3. 收发数据
    Thread(target=reciver, args=(client, )).start()
    while True:
        content = input('')
        if content == 'quit':
            break
        else:
            client.send(content.encode())

    # 6. 关闭套接字
    client.close()


if __name__ == '__main__':
    main()