from socket import *
from struct import *
from threading import *
Mysql = __import__('06 数据库操作')


# 提供一个列表保存所有的在线用户
clients = {}

# 创建一个数据库对象，连接到 chatroom
mysql = Mysql.Mysql('chatroom')


# 线程回调函数: 接收来自另一边的信息
def reciver(sock):
    # 接收目标发送过来的用户名和密码 char[32] + char[32]
    username, password = unpack('32s32s', sock.recv(64))
    username = username.decode('utf-8').strip('\0')
    password = password.decode('utf-8').strip('\0')

    # 查询目标用户名和密码是否匹配
    count, result = mysql.select(f"SELECT * FROM user WHERE username='{username}' AND password=MD5('{password}');")

    # 如果登录成功，就添加到在线列表
    if count == 0:
        sock.send('不ok'.encode())
        return

    if username in clients:
        sock.send('不ok'.encode())
        return
    else:
        sock.send('ok'.encode())
        clients[username] = sock
        print(sock.getpeername(), '连接到了聊天室')

    while True:
        try:
            # 接收客户端发送的数据，由于只是转发，不做解码
            content = sock.recv(100)
            # 遍历在线用户，如果不是发送者就转发
            for client in clients.values():
                if client != sock:
                    client.send(username.encode() + b': ' + content)
        except Exception as e:
            # print('error', e)
            # 客户端或服务器连接中断，需要从列表中移除
            print(sock.getpeername(), '离开了聊天室')
            del clients[username]
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

        # 5. 收发数据
        Thread(target=reciver, args=(client,)).start()


if __name__ == '__main__':
    main()