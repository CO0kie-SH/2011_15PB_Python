from socket import *
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
    server = socket(AF_INET, SOCK_STREAM)

    # 2. 绑定对象到指定的ip和端口
    server.bind(('127.0.0.1', 0x1515))

    # 3. 开启套接字的监听状态
    server.listen(SOMAXCONN)

    # 4. 等待客户端的连接
    client, address = server.accept()

    # 5. 收发数据
    Thread(target=reciver, args=(client, )).start()
    while True:
        content = input('')
        if content == 'quit':
            break
        else:
            client.send(content.encode())

    # 6. 关闭套接字
    client.close()
    server.close()


if __name__ == '__main__':
    main()