from socket import *
from threading import *


# 提供一个列表保存所有的在线用户
clients = []


# 线程回调函数: 接收来自另一边的信息
def reciver(sock):
    while True:
        try:
            # 接收客户端发送的数据，由于只是转发，不做解码
            content = sock.recv(100)
            # 遍历在线用户，如果不是发送者就转发
            for client in clients:
                if client != sock:
                    client.send(content)
        except Exception as e:
            print('error', e)
            # 客户端或服务器连接中断，需要从列表中移除
            print(sock.getpeername(), '离开了聊天室')
            clients.remove(sock)
            # 一定要记得 break 跳出当前的循环
            break


def main():
    # 1. 创建套接字对象
    server = socket(AF_INET, SOCK_STREAM)

    # 2. 绑定对象到指定的ip和端口
    server.bind(('127.0.0.1', 0x1515))

    # 3. 开启套接字的监听状态
    server.listen(SOMAXCONN)

    while True:
        # 4. 等待客户端的连接
        client, address = server.accept()

        clients.append(client)
        print(address, '连接到了聊天室')

        # 5. 收发数据
        Thread(target=reciver, args=(client,)).start()


if __name__ == '__main__':
    main()