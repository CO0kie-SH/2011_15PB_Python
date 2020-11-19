from socket import *


def main():
    # 1. 创建套接字对象
    client = socket(AF_INET, SOCK_STREAM)

    # 2. 等待客户端的连接
    client.connect(('127.0.0.1', 0x1515))

    # 3. 收发数据
    print(client.recv(100).decode('utf-8'))

    # 6. 关闭套接字
    client.close()


if __name__ == '__main__':
    main()