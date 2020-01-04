"""
   题目二
"""
import socket
import threading
from datetime import *
import time
import sys


def main():
    # 1. 创建套接字socket,的标示
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息 bind
    tcp_server_socket.bind(("127.0.0.1", 6661))

    # 3. 让默认的套接字由主动变为被动 listen
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        # 4. 等待别人的电话到来(等待客户端的链接 accept)
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来%s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)  # 注意这个1024byte，大小根据需求自己设置
        print("客户端福送过来的请求是:%s" % recv_data.decode("utf-8"))

        # 回送一部分数据给客户端
        new_client_socket.send("hahahghai-----ok-----".encode("utf-8"))
        # 收到客户端的消息并且能拿到来自客户端的端口号 client_addr 地址


        # 关闭套接字
        # 关闭accept返回的套接字 意味着 不会在为这个客户端服务
        new_client_socket.close()
        print("已经服务器完毕。。。。")

    # 5.关闭客户端的请求
    tcp_server_socket.close()

if __name__ == '__main__':
    main()





