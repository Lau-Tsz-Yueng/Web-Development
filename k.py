# -*- coding:utf-8 -*-
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0",8099))
s.listen(5)
print('server establishing')
while True:
    conn, abbr = s.accept()
    data = conn.recv(1024)
    print(data)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\nHello world')
    conn.close()