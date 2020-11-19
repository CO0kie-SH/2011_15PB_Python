from socket import *


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
    client.send('welcome'.encode('utf-8'))

    # 6. 关闭套接字
    client.close()
    server.close()


if __name__ == '__main__':
    main()