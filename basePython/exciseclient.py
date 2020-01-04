import socket
import threading
from datetime import *
import time
import sys


def sock_client_data():
    while True:
        try:
            # 1. 创建套接字socket,的标示
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 2.服务器和客户端都在一个系统下时使用的ip和端口,建立连接
            s.connect(('127.0.0.1', 6661))
        except socket.error as msg:
            print(msg)
            # 3.客户端退出
            print(sys.exit(1))
        data = input("input data:")   #输入要传输的数据
        s.send(data.encode())  #将要传输的数据编码发送，如果是字符数据就必须要编码发送
        s.close()
if __name__ == '__main__':

    sock_client_data()